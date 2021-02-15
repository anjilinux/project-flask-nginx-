'''  ----------------------------------------------------------------------------------------------------------------

Shannon Equation for Dummies  - JPC Feb 2021

Educational Application - Runs either in local windows or in web pages

The Web version via localhost are fully functional although not as convenient as the windowed version (only 1 plot open)

The Web version in remote does work for a single user (all users connected can send command and see the same page),


--------------------------------------------------------------------------------------------------------------------'''

''' ------------------------------------------ Imports ---------------------------------------------------

The GUI has been designed to be compatible with both PySimpleGUIWeb and PySimpleGUI

The PySimpleGUi version takes full benefit of the matplotlib windowing whereas the Web version is constrained to use 
a web compatible method with only one graph at a time

'''
from math import *
import matplotlib.pyplot as plt
import numpy as np
import webbrowser
import Shannon_Dict as Shd

Web_Version=False  #
Web_Remote=False  #

if Web_Version :
    import PySimpleGUIWeb as sg
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
    import io
    def draw_matfig(fig, element):
        canv = FigureCanvasAgg(fig)
        buf = io.BytesIO()
        canv.print_figure(buf, format='png')
        if buf is None:
            return None
        buf.seek(0)
        data = buf.read()
        element.update(data=data)
    def window_matfig(fig, title_fig, title_win):
        matlayout = [[sg.T(title_fig, font='Any 20')],
                     [sg.Image(key='-IMAGE-')],
                     [sg.B('Exit')]]
        winmat = sg.Window(title_win, matlayout, finalize=True)
        draw_matfig(fig, winmat['-IMAGE-'])  # Web version
        while True:  # Web version
            event, values = winmat.read()
            if event == 'Exit' or event == sg.WIN_CLOSED:
                break
        plt.close()
        winmat.close()
else:
    import PySimpleGUI as sg

if Web_Version and Web_Remote :
    web_cfg={"web_ip":'192.168.1.60',"web_port":8088,"web_start_browser":False}
else:
    web_cfg={}

''' ------------------------------------------ Core Functions ---------------------------------------------------

These functions are mainly application of formulas given in the first panel and formatting functions

'''

def Combine_CNR(*CNR):
    ''' Combination of Carrier to Noise Ratio '''
    NCR_l = 0
    for CNR_dB in CNR:
        NCR_l += 10 ** (-CNR_dB / 10) # Summation of normalized noise variances
    return -10 * log(NCR_l, 10)

def Shannon(BW=36.0, CNR=10.0, Penalty=0.0):
    ''' Shannon Limit, returns Bit Rate '''
    CNR_l = 10 ** ((CNR - Penalty) / 10)
    return BW * log(1 + CNR_l, 2)

def BR_Multiplier(BW_mul=1.0, P_mul=2.0, CNR=10.0):
    ''' Returns BR multiplier  '''
    CNR_l = 10 ** (CNR / 10)
    return BW_mul * log(1 + CNR_l * P_mul / BW_mul, 2) / log(1 + CNR_l, 2)

def Shannon_Points(BW=36.0, CNR=10.0):
    ''' Returns CNR_l, BR_inf, C/N0  and BR(BW,CNR) '''
    CNR_l = 10 ** (CNR / 10)
    C_N0_l = CNR_l * BW
    BR_infinity = C_N0_l / log(2)
    BR_constrained = Shannon(BW, CNR)
    return CNR_l, BR_infinity, C_N0_l, BR_constrained

def Shannon_Sp_Eff(Sp_Eff=0.5, BW=36.0, CNR=10.0):
    ''' Returns values at required Spe : CNR, BW, BR '''
    C_N0_l = 10 ** (CNR / 10) * BW
    BW_Spe_1 = C_N0_l
    BW_Spe = C_N0_l / (2 ** Sp_Eff - 1)
    BR_Spe = BW_Spe * Sp_Eff
    CNR_Spe = 10 * log(BW_Spe_1 / BW_Spe, 10)
    return CNR_Spe, BW_Spe, BR_Spe

def BR_Format(BR=100):
    return "{:.1f}".format(BR) + ' Mbps'

def Power_Format(Pow=100):
    Pow_dB=10*log(Pow,10)
    if  Pow > 1 and Pow < 1e4 :
        return "{:.1f}".format(Pow) + ' W .. ' + "{:.1f}".format(Pow_dB) + ' dBW'
    elif Pow <= 1 and Pow > 1e-3 :
        return "{:.4f}".format(Pow) + ' W .. ' + "{:.1f}".format(Pow_dB) + ' dBW'
    else :
        return "{:.1e}".format(Pow) + ' W .. ' + "{:.1f}".format(Pow_dB) + ' dBW'

def PFD_Format(Pow=1): # PSD in W per m2
    Pow_dB=10*log(Pow,10)
    return "{:.1e}".format(Pow) + ' W/m\N{SUPERSCRIPT TWO} .. ' + "{:.1f}".format(Pow_dB) + ' dBW/m\N{SUPERSCRIPT TWO}'

def PSD_Format(Pow=1):  # PSD in W per MHz
    Pow_dB=10*log(Pow,10)
    return "{:.1e}".format(Pow) + ' W/MHz .. ' + "{:.1f}".format(Pow_dB) + ' dBW/MHz'


def Gain_Format(Gain=1000):
    Gain_dB=10*log(Gain,10)
    return "{:.1f}".format(Gain) + ' .. ' + "{:.1f}".format(Gain_dB) + ' dBi'

def Loss_Format(Loss=10):
    Loss_dB=10*log(Loss,10)
    return "{:.2}".format(Loss) + ' .. ' + "{:.1f}".format(Loss_dB) + ' dB'


''' ------------------------------------------ Main Program ---------------------------------------------------

The program has 2 main panels associated with events collection loops

As the loops are build, when the second panel is open, events are only collected for this panel

In the windowed version, matplotlib plots don't interfere with the event loops : as many as desired can be open
 
'''

form_i={"size":(22,1),"justification":'left',"enable_events":True}   # input format
form_o={"size":(65,1),"justification":'right',"enable_events":True}  # output format, also using input elements

col1=sg.Column([[sg.Frame('Theoretical Exploration',
        [[sg.Text(' Reference C/N [dB] ',**form_i,key='-iCNR-'),sg.Input('12',size=(5,1),key='-CNR-')],
        [sg.Text(' Reference BW [MHz] ',**form_i,key='-iBW-'),sg.Input('36',size=(5,1),key='-BW-')],
        [sg.Text('Power to Noise Power Density Ratio : C/N\N{SUBSCRIPT ZERO}', **form_o,key='-iC_N0-'),
         sg.Input(size=(10,1),key='-C_N0-')],
        [sg.Text('Theoretical BR at infinite BW : 1.44 C/N\N{SUBSCRIPT ZERO}', **form_o,key='-iBRinf-'),
         sg.Input(size=(10,1),key='-BRinf-')],
        [sg.Text('Theoretical BR at Spectral Efficiency = 1 : C/N\N{SUBSCRIPT ZERO}', **form_o,key='-iBRunit-'),
         sg.Input(size=(10,1),key='-BRunit-')],
        [sg.Text('Theoretical BR at Reference (BW,C/N)', **form_o,key='-iBRbw-'),
         sg.Input(size=(10, 1), key='-BRbw-')],
        [sg.Text('C / N = C / (N\N{SUBSCRIPT ZERO}.B) [Linear Format]', **form_o,key='-iCNRlin-'),
         sg.Input(size=(10, 1), key='-CNRlin-')],
        [sg.Text(' BW Increase Factor ',**form_i,key='-iBWmul-'),
         sg.Input('1', size=(5, 1), key='-BWmul-')],
        [sg.Text(' Power Increase Factor ',**form_i,key='-iCmul-'),
         sg.Input('2', size=(5, 1), key='-Cmul-')],
        [sg.Text('Bit Rate Increase Factor', **form_o,key='-iBRmul-'),
         sg.Input(size=(10, 1), key='-BRmul-')],
        [sg.Button('Evaluation', key='-Evaluation-',bind_return_key = True),
         sg.Button('BW Sensitivity',key='-BW_Graph-'),
         sg.Button('Power Sensitivity',key='-Pow_Graph-'),
         sg.Button('BR Factor Map',key='-Map-'),
         sg.Button('Go to Real World',key='-Real-')]],
        )]
        ])

col2=sg.Column([[sg.Frame('Background Information (click on items)',
                [[sg.Multiline('Click on parameter\'s label to get information',size=(70,16),key='-Dialog-')],
                [sg.Button('Advanced'), sg.Button('Write Contribution'),
                 sg.Button('Read Contributions'),sg.Button('Help')]])]])

layout=[[sg.Text('')],
        [sg.Button('https://en.wikipedia.org/wiki/Claude_Shannon',key='-Wiki-')],
        [sg.Image(filename='Shannon.png',key='-iShannon-',enable_events=True, background_color='black')],
        [col1,col2]
        ]

window = sg.Window('Shannon\'s Equation for Dummies', layout , finalize=True, element_justification='center', **web_cfg)

# Needed for the Web version (on a finalized window)
window['-CNR-'].Update('12')
window['-BW-'].Update('36')
window['-BWmul-'].Update('1')
window['-Cmul-'].Update('2')

Win_time_out = 10  # Forces window's reading at first pass

while True:

    event, values = window.read(timeout=Win_time_out, timeout_key='__TIMEOUT__')
    print (event)
    Win_time_out = None

    try:

        if event == sg.WIN_CLOSED: # if user closes window
            break

        elif event == '-Evaluation-' or event == '__TIMEOUT__' :

            if event == '__TIMEOUT__' :
                window['-Dialog-'].Update(Shd.Help['-iShannon-'])  # Display at first pass

            CNR_Nyq=float(values['-CNR-'])
            BW_Nyq=float(values['-BW-'])

            CNR_l, BRinf, C_N0_l, BRbw = Shannon_Points(BW_Nyq,CNR_Nyq)

            BRunit = C_N0_l  # Mbps / MHz : Sp Eff =1

            window['-C_N0-'].Update("{:.1f}".format(C_N0_l) + ' MHz')
            window['-BRinf-'].Update(BR_Format(BRinf))
            window['-BRunit-'].Update(BR_Format(BRunit))
            window['-BRbw-'].Update(BR_Format(BRbw))
            window['-CNRlin-'].Update("{:.1f}".format(CNR_l))

            BWmul=float(values['-BWmul-'])
            Cmul=float(values['-Cmul-'])

            BRmul=BR_Multiplier(BWmul,Cmul,CNR_Nyq)
            window['-BRmul-'].Update("{:.2f}".format(BRmul))

        elif event == '-Wiki-':
            webbrowser.open('https://en.wikipedia.org/wiki/Claude_Shannon')

        elif event in ('-iC_N0-','-iCNR-','-iBRinf-','-iBRunit-','-iBRbw-','-iCNRlin-','-iBRmul-','-iCmul-',
                       '-iBWmul-','-iBW-','-iShannon-','Advanced','Help' ):
            window['-Dialog-'].Update(Shd.Help[event])

        elif event == '-BW_Graph-':
            BW = np.zeros(20)
            BR = np.zeros(20)
            CNR = np.zeros(20)
            CNR[0] = CNR_Nyq + 10 * log(2, 10)
            BW[0] = BW_Nyq / 2
            BR[0] = Shannon(BW[0], CNR[0])
            for i in range(1, 20):
                BW[i] = BW[i - 1] * 2 ** (1 / 3)
                CNR[i] = CNR[i - 1] - 10 * log(BW[i] / BW[i - 1], 10)
                BR[i] = Shannon(BW[i], CNR[i])
            fig = plt.figure(figsize=(6, 4))
            ax = fig.add_subplot(111)
            plt.plot(BW, BR, 'b')
            Mark = ('D', 's', 'p', 'h', 'x')
            for i in range(5):
                ind = 3 * (i + 1)
                BR_norm = BR[ind] / BR[3]
                plt.plot(BW[ind], BR[ind], Mark[i] + 'b', label="{:.1f}".format(BW[ind]) + " MHz" +
                                            "  ,  {:.1f}".format(BR[ind]) + " Mbps" + " : {:.0%}".format(BR_norm))
            plt.title('Theoretical Bit Rate at Constant C/N\N{SUBSCRIPT ZERO} =  ' + "{:.1f}".format(C_N0_l) + " MHz" )
            plt.xlabel('Bandwidth [MHz]')
            plt.ylabel('Bit Rate [Mbps]')
            plt.grid(True)
            plt.legend(loc='lower right')

            if Web_Version:
                window_matfig(fig, title_fig='Bandwidth Sensitivity', title_win='Shannon for Dummies')
            else:
                plt.show(block=False)

        elif event == '-Pow_Graph-':
            SNR = np.zeros(20)
            BR = np.zeros(20)
            CNR = np.zeros(20)
            SNR[0] = 10 ** ( CNR_Nyq / 10 ) / 8  #Linear Format
            CNR[0] = CNR_Nyq - 10 * log(8, 10)
            BR[0] = Shannon(BW_Nyq, CNR[0])
            for i in range(1, 20):
                SNR[i] = SNR[i-1] * 2 ** ( 1 / 3 )
                CNR[i] = CNR[i - 1] + 10 * log( 2 ** ( 1 / 3 ), 10 )
                BR[i] = Shannon(BW_Nyq, CNR[i])
            fig = plt.figure(figsize=(6, 4))
            ax = fig.add_subplot(111)
            plt.plot(SNR, BR, 'b')
            Mark = ('D', 's', 'p', 'h', 'x')
            for i in range(5):
                ind = 3 * (i + 1)
                BR_norm = BR[ind] / BR[9]
                plt.plot(SNR[ind], BR[ind], Mark[i] + 'b', label="{:.1f}".format(SNR[ind]) +
                            "x   ,  {:.1f}".format(BR[ind]) + " Mbps" + " : {:.0%}".format(BR_norm))
            plt.title('Theoretical Bit Rate at Constant Bandwidth : ' + "{:.1f}".format(BW_Nyq) + " MHz")
            plt.xlabel('Signal Power to Noise Power Ratio [ Linear ]')
            plt.ylabel('Bit Rate [Mbps]')
            plt.grid(True)
            plt.legend(loc='lower right')

            if Web_Version:
                window_matfig(fig, title_fig='Power Sensitivity', title_win='Shannon for Dummies')
            else:
                plt.show(block=False)

        elif event == '-Map-' :
            BR_mul=np.zeros((21,21))
            BW_mul=np.zeros((21,21))
            P_mul=np.zeros((21,21))
            for i in range(21):
                for j in range(21):
                    BW_mul[i, j] = (i + 1)/4
                    P_mul[i, j] = (j + 1)/4
                    BR_mul[i, j] = BR_Multiplier(BW_mul[i, j], P_mul[i, j], CNR_Nyq)
            fig = plt.figure(figsize=(6, 4))
            ax = fig.add_subplot(111)
            Map = plt.contour(BW_mul,P_mul,BR_mul, 20)
            plt.clabel(Map, inline=1, fontsize=8,fmt='%.2f')
            plt.title('Bit Rate Multiplying Factor, \n Reference : C/N =  {:.1f}'.format(CNR_Nyq) + ' dB, BW = ' +
                      '{:.1f}'.format(BW_Nyq) + ' MHz , C/N\N{SUBSCRIPT ZERO} = ' + '{:.1f}'.format(C_N0_l) +
                      ' MHz, BR = {:.1f}'.format(BRbw) + ' Mbps', fontsize=10)
            plt.xlabel('Bandwidth Multiplying Factor')
            plt.ylabel('Power Multiplying Factor')
            plt.grid(True)

            if Web_Version:
                window_matfig(fig, title_fig='Multiplying Factors Map', title_win='Shannon for Dummies')
            else:
                plt.show(block=False)

        elif event == '-Real-': # ---------------- Opening of Second Window -------------------

            fr1 = sg.Frame('Satellite Link',[
                    [sg.Text('Frequency  [GHz]',**form_i,key='-iFreq-'),
                     sg.Input('12', size=(5, 1), key='-Freq-'),
                    sg.Text('HPA Output Power [W]',**form_i,key='-iHPA-'),
                     sg.Input('120', size=(5, 1), key='-HPA_P-')],
                    [sg.Text('Output Losses [dB]',**form_i,key='-iLoss-'),
                     sg.Input('2', size=(5, 1), key='-Losses-'),
                    sg.Text('Impairments C/I [dB]', **form_i, key='-iSCIR-'),
                     sg.Input('20', size=(5, 1), key='-Sat_CIR-')],
                    [sg.Text('Beam Diameter [\N{DEGREE SIGN}]',**form_i,key='-iSBeam-'),
                     sg.Input('3', size=(5, 1), key='-Sat_Beam-'),
                    sg.Text('Offset from Peak [dB] ',**form_i,key='-iGOff-'),
                     sg.Input('0', size=(5, 1), key='-Gain_Offset-')],
                    [sg.Text('Path Length [km] ​',**form_i,key='-iPath-'),
                     sg.Input('38000', size=(5, 1), key='-Path_Length-'),
                    sg.Text('Rain & Gaz Attenuation [dB] ​',**form_i,key='-iFade-'),
                     sg.Input('0.6', size=(5, 1), key='-Rain_Fade-')],
                    [sg.Text('Output Power', **form_o,key='-iOPow-'),
                    sg.Input('', size=(35, 1), key='-Feed_P-', justification='center')],
                    [sg.Text('Satellite Antenna Gain​', **form_o,key='-iSGain-'),
                    sg.Input('', size=(35, 1), key='-Sat_G-', justification='center')],
                    [sg.Text('Equivalent Isotropic Radiated Power​', **form_o,key='-iEIRP-'),
                    sg.Input('', size=(35, 1), key='-EIRP-', justification='center')],
                    [sg.Text('Free Space Loss', **form_o, key='-iPLoss-'),
                    sg.Input('', size=(35, 1), key='-PLoss-', justification='center')],
                    [sg.Text('Power Flux Density', **form_o,key='-iPFD-'),
                    sg.Input('', size=(35, 1), key='-PFD-', justification='center')],
                    ])


            fr2=sg.Frame('Radio Front End ',[
                    [sg.Text('Customer Antenna Size [m] ​',**form_i,key='-iCPE-'),
                     sg.Input('0.6', size=(5, 1), key='-CPE_Ant-'),
                     sg.Text('Noise Temperature [K] ​', **form_i, key='-iCPE_T-'),
                     sg.Input('140', size=(5, 1), key='-CPE_T-')],
                    [sg.Text('Customer Antenna Effective Area and G/T', **form_o,key='-iCGain-'),
                    sg.Input('', size=(35, 1), key='-CPE_G-', justification='center')],
                    [sg.Text('RX Power at Antenna Output', **form_o,key='-iRXPow-'),
                    sg.Input('', size=(35, 1), key='-RX_P-', justification='center')],
                    [sg.Text('Noise Power Density Antenna Output', **form_o, key='-iN0-'),
                    sg.Input('', size=(35, 1), key='-N0-', justification='center')],
                    [sg.Text('Bit Rate at infinite Bandwidth', **form_o,key='-iBRinf-'),
                    sg.Input('', size=(35, 1), key='-BRinf-', justification='center')],
                    [sg.Text('Bit Rate at Spectral Efficiency=1/2', **form_o,key='-iBRhalf-'),
                    sg.Input('', size=(35, 1), key='-BRhalf-', justification='center')],
                    [sg.Text('Bit Rate at Spectral Efficiency=1', **form_o,key='-iBRUnit-'),
                    sg.Input('', size=(35, 1), key='-BRUnit-', justification='center')],
                    [sg.Text('Bit Rate at Spectral Efficiency=2', **form_o,key='-iBRdouble-'),
                    sg.Input('', size=(35, 1), key='-BRdouble-', justification='center')],
                    ])


            fr3=sg.Frame('Baseband Unit',[
                    [sg.Text('Available Bandwidth [MHz]',**form_i,key='-iBW-'),
                     sg.Input('36', size=(5, 1), key='-BW-'),
                    sg.Text('Nyquist Filter Rolloff [%]',**form_i,key='-iRO-'),
                     sg.Input('5', size=(5, 1), key='-RO-')],
                    [sg.Text('Signal Impairments C/I [dB]',**form_i,key='-iCIR-'),
                     sg.Input('20', size=(5, 1), key='-CIR-'),
                    sg.Text('Code Penalty vs theory [dB]​',**form_i,key='-iPenalty-'),
                     sg.Input('1', size=(5, 1), key='-Penalty-')],
                    [sg.Text('Higher Layers Overhead [%]',**form_i,key='-iOH-'),
                     sg.Input('5', size=(5, 1), key='-OH-')],
                    [sg.Text('Nyquist Bandwidth', **form_o,key='-iNBW-'),
                    sg.Input('', size=(35, 1), key='-N_BW-', justification='center')],
                    [sg.Text('Signal to Noise Ratio in Available BW', **form_o,key='-iCNRbw-'),
                    sg.Input('', size=(35, 1), key='-CNRbw-', justification='center')],
                    [sg.Text('Signal to Noise Ratio in Nyquist BW', **form_o,key='-iCNRnyq-'),
                    sg.Input('', size=(35, 1), key='-CNRnyq-', justification='center')],
                    [sg.Text('Signal to Noise Ratio at Receiver Output', **form_o,key='-iCNRrcv-'),
                    sg.Input('', size=(35, 1), key='-CNRrcv-', justification='center')],
                    [sg.Text('Theoretical Bit Rate in Available BW', **form_o,key='-iBRbw-'),
                    sg.Input('', size=(35, 1), key='-BRbw-', justification='center')],
                    [sg.Text('Theoretical Bit Rate in Nyquist BW', **form_o,key='-iBRnyq-'),
                    sg.Input('', size=(35, 1), key='-BRnyq-', justification='center')],
                    [sg.Text('Practical Bit Rate in Nyquist BW', **form_o,key='-iBRrcv-'),
                    sg.Input('', size=(35, 1), key='-BRrcv-', justification='center')],
                    [sg.Text('Practical Higher Layers Bit Rate', **form_o,key='-iBRhigh-'),
                    sg.Input('', size=(35, 1), key='-BRhigh-', justification='center')],
                    [sg.Button('Evaluation', key='-Evaluation-',bind_return_key = True),
                    sg.Button('BW Sensitivity',key='-BW_Graph-'),
                    sg.Button('Power Sensitivity',key='-Pow_Graph-'),
                    sg.Button('BR Factor Map', key='-Map-'),
                    sg.Button('Back to Theory', key='-Back-')],
                    ])

            fr4 = sg.Frame('Background Information (click on items)',
                    [[sg.Multiline('Click on parameter\'s label to get information', size=(70, 16),key='-Dialog-')],
                    [sg.Button('Advanced'), sg.Button('Write Contribution'),
                    sg.Button('Read Contributions'), sg.Button('Help')]])


            layout2 =[[sg.Text('')],
                    [sg.Column([[fr1],[fr2],[fr3]]),
                    sg.Column([[sg.Button('wiki : Harry Nyquist​', size=(25,1), key='-W_Nyquist-'),
                    sg.Button('wiki : Richard Hamming​', size=(25,1), key='-W_Hamming-')],
                    [sg.Button('wiki : Andrew Viterbi​', size=(25,1), key='-W_Viterbi-'),
                    sg.Button('wiki : Claude Berrou​', size=(25,1), key='-W_Berrou-')],
                    [sg.Image(filename='Satellite.png', key='-Satellite-',background_color='black', enable_events=True)],
                    [fr4]],element_justification='center')]]

            window2 = sg.Window('Shannon and Friends in the Real World', layout2, finalize=True)

            # Needed for the Web version (on a finalized window)
            window2['-Freq-'].Update('12')
            window2['-HPA_P-'].Update('120')
            window2['-Sat_CIR-'].Update('20')
            window2['-Losses-'].Update('2')
            window2['-Sat_Beam-'].Update('3')
            window2['-Gain_Offset-'].Update('0')
            window2['-Path_Length-'].Update('38000')
            window2['-Rain_Fade-'].Update('0.6')
            window2['-CPE_Ant-'].Update('0.6')
            window2['-CPE_T-'].Update('120')
            window2['-Penalty-'].Update('1')
            window2['-BW-'].Update('36')
            window2['-CIR-'].Update('25')
            window2['-RO-'].Update('5')
            window2['-OH-'].Update('5')

            Win_time_out=10  # Forces window's reading at first pass

            while True:

                event, values = window2.read(timeout=Win_time_out,timeout_key = '__TIMEOUT__')
                print(event)
                Win_time_out=None

                try:

                    if event == sg.WIN_CLOSED or event== '-Back-':  # closes window
                        break

                    elif event == '-Evaluation-'or event == '__TIMEOUT__' :

                        if event == '__TIMEOUT__':
                            window2['-Dialog-'].Update(Shd.Help2['-Satellite-'])  # Display Help at first pass

                        Freq = float(values['-Freq-']) # GHz
                        HPA_Power = float(values['-HPA_P-']) # Watts
                        Sat_Loss = float(values['-Losses-'])  # dB
                        Sat_CIR = float(values['-Sat_CIR-'])  # dB
                        Sig_Power = HPA_Power * 10 ** (-Sat_Loss / 10)  # Watts
                        Sat_Beam = float(values['-Sat_Beam-'])  #dB
                        Gain_Offset = float(values['-Gain_Offset-'])  #dB
                        Sat_Ant_eff = 0.6
                        Path_Length = float(values['-Path_Length-'])  # kilometer
                        Rain_Fade = float(values['-Rain_Fade-'])  #dB
                        Athmo_Loss = 0.6  # dB
                        window2['-Feed_P-'].Update(Power_Format(Sig_Power))

                        Lambda = 300e6 / Freq / 1e9  # meter
                        Sat_Gain_l = Sat_Ant_eff * ( pi * 70 / Sat_Beam ) ** 2 # Formula to be
                        Sat_Gain_l = Sat_Gain_l * 10**(-Gain_Offset/10)
                        Sat_Ant_d = 70 * Lambda / Sat_Beam
                        Sat_Gain_dB = 10 * log(Sat_Gain_l, 10)

                        window2['-Sat_G-'].Update(Gain_Format(Sat_Gain_l))

                        EIRP_l = Sig_Power * Sat_Gain_l
                        EIRP_dB = 10 * log(EIRP_l, 10)
                        window2['-EIRP-'].Update(Power_Format(EIRP_l))

                        Path_Loss_l = (4 * pi * Path_Length * 1000 / Lambda) ** 2
                        Path_Loss_dB = 10 * log(Path_Loss_l, 10)
                        window2['-PLoss-'].Update(Loss_Format(Path_Loss_l)+'m\N{SUPERSCRIPT TWO}')

                        PFD_l = EIRP_l / (4 * pi * (Path_Length * 1000) ** 2) * 10 ** (-(Athmo_Loss+Rain_Fade)/ 10)
                        PFD_dB = 10 * log(PFD_l, 10)
                        window2['-PFD-'].Update(PFD_Format(PFD_l))

                        CPE_Ant_d = float(values['-CPE_Ant-'])  # meter
                        CPE_T_Clear= float(values['-CPE_T-'])  # K
                        CPE_Ant_eff = 0.6
                        CPE_T_Att = (CPE_T_Clear - 40) + 40 * 10 ** (-Rain_Fade/10) + 290 * ( 1 - 10 ** (-Rain_Fade/10))
                        k_Boltz = 1.38e-23  # J/K
                        Penalties = float(values['-Penalty-'])  # dB, code penalty
                        Bandwidth = float(values['-BW-'])  # MHz
                        CNR_Imp = float(values['-CIR-'])  # dB
                        Rolloff = float(values['-RO-'])  # percent
                        Overheads = float(values['-OH-'])  # percent

                        CPE_Ae = pi * CPE_Ant_d ** 2 / 4 * CPE_Ant_eff
                        CPE_Gain_l = (pi * CPE_Ant_d / Lambda) ** 2 * CPE_Ant_eff
                        CPE_Gain_dB = 10 * log(CPE_Gain_l, 10)
                        CPE_Beam = 70 * Lambda / CPE_Ant_d  # diameter in degrees
                        CPE_G_T = 10 * log(CPE_Gain_l / CPE_T_Att, 10)
                        window2['-CPE_G-'].Update(
                            "{:.1f}".format(CPE_Ae)+" m\N{SUPERSCRIPT TWO} .. {:.1f}".format(CPE_G_T)+" dB/K")

                        RX_Power_l = PFD_l * CPE_Ae  # Alternative : RX_Power_l=EIRP_l/Path_Loss_l*CPE_Gain_l
                        RX_Power_dB = 10 * log(RX_Power_l,10)
                        N0 = k_Boltz * CPE_T_Att  # W/Hz
                        C_N0_l = RX_Power_l / N0  # Hz
                        C_N0_dB = 10 * log(C_N0_l, 10)  # dBHz
                        window2['-RX_P-'].Update('C : ' + Power_Format(RX_Power_l))
                        window2['-N0-'].Update('N\N{SUBSCRIPT ZERO} : ' + PSD_Format(N0*1e6))

                        BW_Spe_1 = C_N0_l / 1e6  # C_N0 without Penalty in MHz
                        BW_Spe_1half = BW_Spe_1 / (2 ** 0.5 - 1)  # MHz
                        BW_Spe_1quarter = BW_Spe_1 / (2 ** 0.25 - 1)
                        BW_Spe_double = BW_Spe_1 / (2 ** 2 - 1)

                        BR_Spe_1 = BW_Spe_1  # Mbps
                        BR_Spe_1half = BW_Spe_1half / 2
                        BR_Spe_1quarter = BW_Spe_1quarter / 4
                        BR_Spe_double= BW_Spe_double * 2
                        BR_infinity = BW_Spe_1 / log(2)
                        BR_Spe_1_Norm = BR_Spe_1 / BR_infinity
                        BR_Spe_1half_Norm = BR_Spe_1half / BR_infinity
                        BR_Spe_1quarter_Norm = BR_Spe_1quarter / BR_infinity
                        BR_Spe_double_Norm = BR_Spe_double / BR_infinity
                        window2['-BRinf-'].Update('1.443 C/N\N{SUBSCRIPT ZERO} : ' +
                                                BR_Format(BR_infinity)+" .. {:.0%}".format(1))
                        window2['-BRhalf-'].Update('1.207 C/N\N{SUBSCRIPT ZERO} : ' +
                                                BR_Format(BR_Spe_1half) + " .. {:.0%}".format(BR_Spe_1half_Norm))
                        window2['-BRUnit-'].Update('C/N\N{SUBSCRIPT ZERO} : ' +
                                                BR_Format(BR_Spe_1)+" .. {:.0%}".format(BR_Spe_1_Norm))
                        window2['-BRdouble-'].Update('0.667 C/N\N{SUBSCRIPT ZERO} : ' +
                                                BR_Format(BR_Spe_double)+" .. {:.0%}".format(BR_Spe_double_Norm))

                        CNR_Spe_1 = 0  # dB
                        CNR_Spe_1half = -10 * log(BW_Spe_1half / BW_Spe_1, 10)
                        CNR_Spe_1quarter = -10 * log(BW_Spe_1quarter / BW_Spe_1, 10)
                        CNR_Spe_double = -10 * log(BW_Spe_double/ BW_Spe_1, 10)

                        CNR_BW = CNR_Spe_1 + 10 * log(BW_Spe_1 / Bandwidth, 10)  # dB
                        BW_Nyq = Bandwidth / (1 + Rolloff / 100)  # MHz
                        CNR_Nyq = CNR_Spe_1 + 10 * log(BW_Spe_1 / BW_Nyq, 10)  # dBB
                        CNR_Rcv = Combine_CNR (CNR_Nyq, CNR_Imp, Sat_CIR)  #
                        BR_BW = Shannon (Bandwidth, CNR_BW)  # Mbps
                        BR_Nyq = Shannon (BW_Nyq, CNR_Nyq)  # Mbps
                        BR_Rcv = Shannon (BW_Nyq, CNR_Rcv,Penalties)  # Mbps
                        BR_Rcv_Higher = BR_Rcv / (1 + Overheads / 100)  # Mbps
                        BR_BW_Norm = BR_BW / BR_infinity
                        BR_Nyq_Norm = BR_Nyq / BR_infinity
                        BR_Rcv_Norm = BR_Rcv / BR_infinity
                        BR_Rcv_H_Norm = BR_Rcv_Higher / BR_infinity
                        Spe_BW = BR_BW / Bandwidth
                        Spe_Nyq = BR_Nyq / Bandwidth  # Efficiency in available bandwidth
                        Bits_per_Symbol = BR_Nyq / BW_Nyq  # Efficiency in Nyquist bandwidth
                        Spe_Rcv = BR_Rcv / Bandwidth
                        Spe_Higher = BR_Rcv_Higher / Bandwidth

                        window2['-N_BW-'].Update("{:.1f}".format(BW_Nyq) + ' MHz')
                        window2['-CNRbw-'].Update("{:.1f}".format(CNR_BW)+" dB")
                        window2['-CNRnyq-'].Update("{:.1f}".format(CNR_Nyq)+" dB")
                        window2['-CNRrcv-'].Update("{:.1f}".format(CNR_Rcv)+" dB")
                        window2['-BRbw-'].Update(BR_Format(BR_BW)+" .. {:.0%}".format(BR_BW_Norm)+
                                        " .. {:.1f}".format(Spe_BW)+" bps/Hz")
                        window2['-BRnyq-'].Update(BR_Format(BR_Nyq) + " .. {:.0%}".format(BR_Nyq_Norm)+
                                        " .. {:.1f}".format(Bits_per_Symbol)+" b/S .. {:.1f}".format(Spe_Nyq)+" bps/Hz")
                        window2['-BRrcv-'].Update(BR_Format(BR_Rcv) + " .. {:.0%}".format(BR_Rcv_Norm)+
                                        " .. {:.1f}".format(Spe_Rcv)+" bps/Hz")
                        window2['-BRhigh-'].Update(BR_Format(BR_Rcv_Higher)+" .. {:.0%}".format(BR_Rcv_H_Norm)+
                                        " .. {:.1f}".format(Spe_Higher)+" bps/Hz")

                    elif event in ('-iFreq-','-iHPA-','-iSBeam-','-iPath-', '-iLoss-', '-iGOff-','-iFade-', '-iSCIR-',
                                      '-iOPow-','-iSGain-', '-iEIRP-', '-iPFD-', '-iCPE-','-iCGain-','-iRXPow-',
                                      '-iBRinf-','-iBRhalf-', '-iBRUnit-','-iBRdouble-','-iBW-','-iRO-','-iCIR-',
                                      '-iPenalty-', '-iOH-','-iNBW-', '-iCNRbw-','-iCNRnyq-','-iCNRrcv-','-iBRbw-',
                                      '-iBRnyq-','-iBRrcv-','-iBRhigh-','-Satellite-','-iPLoss-','Advanced','Help',
                                      '-iN0-', '-iCPE_T-'):
                        window2['-Dialog-'].Update(Shd.Help2[event])
                    elif event == '-BW_Graph-' :
                        BW = np.zeros(20)
                        BR = np.zeros(20)
                        CNR = np.zeros(20)
                        CNR[0] = CNR_Nyq+10*log(2,10)
                        BW[0] = Bandwidth/2
                        BR[0] = Shannon(BW[0]/(1+Rolloff/100), CNR[0], Penalties) / (1 + Overheads / 100)
                        for i in range(1, 20):
                            BW[i] = BW[i - 1] * 2 ** (1 / 3)
                            CNR[i] = CNR[i - 1] - 10 * log(BW[i] / BW[i - 1], 10)
                            CNR_Rcv_i = Combine_CNR(CNR[i], CNR_Imp, Sat_CIR)
                            BR[i] = Shannon(BW[i]/(1+Rolloff/100), CNR_Rcv_i, Penalties) / (1 + Overheads / 100)

                        fig = plt.figure(figsize=(6, 4))
                        ax = fig.add_subplot(111)
                        plt.plot(BW, BR, 'b')
                        Mark = ('D', 's', 'p', 'h', 'x')
                        for i in range(5):
                            ind = 3 * (i + 1)
                            BR_norm = BR[ind] / BR[3]
                            plt.plot(BW[ind], BR[ind], Mark[i] + 'b',label="{:.1f}".format(BW[ind]) +
                                        " MHz" + "  ,  {:.1f}".format(BR[ind]) + " Mbps" + " : {:.0%}".format(BR_norm))
                        plt.title('Practical Higher Layers Bit Rate at Constant Power : ' +
                                        "{:.1f}".format(HPA_Power) + " W")
                        plt.xlabel('Bandwidth [MHz]')
                        plt.ylabel('Bit Rate [Mbps]')
                        plt.grid(True)
                        plt.legend(loc='lower right')

                        if Web_Version:
                            window_matfig(fig, title_fig='Bandwidth Sensitivity',
                                          title_win='Shannon and Friends in the Real World')
                        else:
                            plt.show(block=False)

                    elif event == '-Pow_Graph-' :
                        Power = np.zeros(20)
                        BR = np.zeros(20)
                        CNR = np.zeros(20)
                        Power[0] = HPA_Power / 8
                        CNR[0] = CNR_Nyq-10*log(8,10)
                        CNR_Rcv_i = Combine_CNR(CNR[0], CNR_Imp, Sat_CIR)
                        BR[0] = Shannon(BW_Nyq, CNR_Rcv_i, Penalties) / (1 + Overheads / 100)
                        for i in range(1, 20):
                            Power[i] = Power[i-1] * 2 ** (1 / 3)
                            CNR[i] = CNR[i - 1] + 10 * log( 2 ** (1 / 3) , 10 )
                            CNR_Rcv_i = Combine_CNR(CNR[i], CNR_Imp, Sat_CIR)
                            BR[i] = Shannon(BW_Nyq, CNR_Rcv_i, Penalties) / (1 + Overheads / 100)
                        fig = plt.figure(figsize=(6, 4))
                        ax = fig.add_subplot(111)
                        plt.plot(Power, BR, 'b')
                        Mark = ('D', 's', 'p', 'h', 'x')
                        for i in range(5):
                            ind = 3 * (i + 1)
                            BR_norm=BR[ind]/BR[9]
                            plt.plot(Power[ind], BR[ind], Mark[i] + 'b', label="{:.1f}".format(Power[ind]) + " W" +
                                                "  ,  {:.1f}".format(BR[ind]) + " Mbps"+" : {:.0%}".format(BR_norm))
                        plt.title('Practical Higher Layers Bit Rate at Constant Bandwidth : ' +
                                                "{:.1f}".format(Bandwidth) + " MHz")
                        plt.xlabel('Power [Watts]')
                        plt.ylabel('Bit Rate [Mbps]')
                        plt.grid(True)
                        plt.legend(loc='lower right')

                        if Web_Version:
                            window_matfig(fig, title_fig='Power Sensitivity',
                                          title_win='Shannon and Friends in the Real World')
                        else:
                            plt.show(block=False)

                    elif event == '-Map-':
                        BR_mul = np.zeros((21, 21))
                        BW_mul = np.zeros((21, 21))
                        P_mul = np.zeros((21, 21))
                        BR_00 = BR_Rcv_Higher
                        for i in range(21):
                            for j in range(21):
                                BW_mul[i, j] = (i + 1) / 4
                                P_mul[i, j] = (j + 1) / 4
                                CNR_ij = CNR_Nyq + 10 * log( P_mul[i, j] / BW_mul[i, j] , 10 )
                                CNR_Rcv_ij = Combine_CNR (CNR_ij, CNR_Imp, Sat_CIR)
                                BW_ij = BW_Nyq * BW_mul[i, j]
                                BR_ij = Shannon( BW_ij / (1 + Rolloff / 100), CNR_Rcv_ij, Penalties) / (1 + Overheads / 100)
                                BR_mul[i, j] = BR_ij / BR_00
                        fig = plt.figure(figsize=(6, 4))
                        ax = fig.add_subplot(111)
                        Map = plt.contour(BW_mul, P_mul, BR_mul, 20)
                        plt.clabel(Map, inline=1, fontsize=8, fmt='%.2f')
                        plt.title('Bit Rate Multiplying Factor, \n Reference :  Power =  {:.1f}'.format(HPA_Power) +
                                  ' W , BW = ' + '{:.1f}'.format(Bandwidth) +
                                  ' MHz , BR = {:.1f}'.format(BR_Rcv_Higher) + ' Mbps')
                        plt.xlabel('Bandwidth Multiplying Factor')
                        plt.ylabel('Power Multiplying Factor')
                        plt.grid(True)

                        if Web_Version:
                            window_matfig(fig, title_fig='Multiplying Factors Map',
                                          title_win='Shannon and Friends in the Real World')
                        else:
                            plt.show(block=False)

                    elif event == '-W_Nyquist-':
                        webbrowser.open('https://en.wikipedia.org/wiki/Harry_Nyquist')
                    elif event == '-W_Hamming-':
                        webbrowser.open('https://en.wikipedia.org/wiki/Richard_Hamming​')
                    elif event == '-W_Viterbi-':
                        webbrowser.open('https://en.wikipedia.org/wiki/Andrew_Viterbi')
                    elif event == '-W_Berrou-':
                        webbrowser.open('https://en.wikipedia.org/wiki/Claude_Berrou​')

                except ValueError:
                    print(sg.popup_ok('Input fields only support numerical values'))

            print(window2.close())
            Win_time_out = 10  # Forces first window's reading at return from second window

    except ValueError:
        print(sg.popup_ok('Input fields only support numerical values'))

window.close()

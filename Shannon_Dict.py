
Help={'-iCNR-':'Reference C/N [dB]\n\nReference Carrier to Noise Ratio in decibels : 10 log (C/N), where C is the '
               'Carrier\'s power or Signal\'s Power and N is the Noise\'s Power, both are measured in the reference '
               'Channel Bandwidth',
    '-iC_N0-':'Power to Noise Power Density Ratio : C/N\N{SUBSCRIPT ZERO}\n\nCarrier\'s power (in Watts) divided by '
              'the Noise Spectral Power Density (in Watts per MHz), the result\'s units are MHz',
    '-iBRinf-':'Theoretical BR at infinite BW : 1.44 C/N\N{SUBSCRIPT ZERO}\n\nBit Rate theoretically achievable when '
               'the signal occupies an infinite Bandwidth, this value is a useful asympotical limit',
    '-iBRunit-':'Theoretical BR at Spectral Efficiency = 1 : C/N\N{SUBSCRIPT ZERO}\n\nBit Rate theoretically '
                'achievable at a Spectral Efficiency = 1. The corresponding value, deduced from the Shannon\'s '
                'formula is given by C/N\N{SUBSCRIPT ZERO}',
    '-iBRbw-':'Theoretical BR at Reference (BW,C/N)\n\nBit Rate theoretically achievable when the Bandwidth is '
              'constrained to the given value',
    '-iCNRlin-':'C / N = C / (N\N{SUBSCRIPT ZERO}.B) [Linear Format]\n\nReference Carrier to Noise Ratio in linear '
                'format, it\'s the value used in the Shannon\'s formula',
    '-iBRmul-':'Bit Rate Increase Factor\n\nBit Rate multiplying factor achieved when the Bandwidth and the Power '
               'and multiplied by a given set of values',
    '-iCmul-':'Power Increase Factor\n\nArbitrary multiplying factor applied to the Carrier\'s Power, for '
              'sensitivity analysis',
    '-iBWmul-':'BW Increase Factor\n\nArbitrary multiplying factor applied to the Carrier\'s Bandwidth, for '
               'sensitivity analysis',
    '-iBW-':'Reference BW [MHz]\n\nReference Channel Bandwidth, this is a key parameter of the communication channel',
    'Advanced': 'The model assumes that the communication channel is \"AWGN\", just Adding White Gaussian Noise to '
        'the signal. This noise is supposed to be random and white which means that noise at a given time is '
        'independent of noise at any other time, this implies that the noise has a flat and infinite spectrum.'
        'This noise is also supposed to be Gaussian which means that its probability density function follows a '
        'Gaussian law, with a variance associated to the Noise\'s power.\n\n'
        'Although these assumptions seem very strong, they are quite accurately matching the cases of interest. '
        'Many impairments are actually non linear and/or non additive, but just combining equivalent C/N of all '
        'impairments as if they were fully AWGN is in most of the cases very accurate.'
        'The reason for that is that the sum of random variables of unknown laws always tend to Gaussian and that '
        'in most system thermal noise is dominating, is actually white and gaussian and is whitening the rest.\n\n'
        'In satellite systems, the noise is mainly coming from the electronics of the radio front end, the ground '
        'seen by the antenna, the stars and the atmospheric attenuator. In case of rain, the signal is punished twice '
        ': the attenuation makes it weaker and the rain attenuator generates noise added to the overall noise.\n\n'
        'Overall the Shannon Limit is a pretty convenient tool to predict the real performances of communication '
        'systems and even more importantly to get a sense of the role of the key design parameters.',
    '-iShannon-':'The Shannon Limit allows to evaluate the theoretical capacity achievable over a communication '
        'channel.\n\nAs a true genius, Claude Shannon has funded the communication theory, the information theory '
        'and more (click the Wikipedia button for more info).\n\nThis equation is fundamental for the evaluation of '
        'communication systems. It is an apparently simple but extremely powerful tool to guide communication systems\''
        ' designs.\n\nThis equation tells us what is achievable, not how to achieve it. It took almost 50 years to '
        'approach this limit with the invention of Turbo codes.\n\nIn the satellite domain, DVB-S2x, using LDPC codes '
        'iteratively decoded (Turbo-Like), is only 1 dB away from this limit.',
    'Help': 'Recommendations for using the tool\n\nThe first purpose of the tool is educational, allowing people to '
            'better understand the physics of communications and the role of key parameters.\n\n'
            'The user should try multiple values in all the fields one per one, explore the graphs and try to '
            'understand the underlying physics.\n\n'
            'The units for the different figures are as explicit as possible to facilitate the exploration.\n\n'
            'All labels can be \"clicked\" to get information about associated item. All values (including this text)'
            ' can be copy/pasted for further usage.'
    }

Help2={'-iFreq-':'Frequency [GHz]\n\nFrequency of the electromagnetic wave supporting the communication in GHz '
                 '(billions of cycles per second).\n\nFor satellite downlink (satellite to terminal), frequency bands '
                 'and frequencies are typically : L : 1.5 GHz , S : 2.2 GHz , C : 4 GHz , Ku : 12 GHz, Ka : 19 GHz, '
                 'Q : 40 GHz',
        '-iHPA-':'HPA Power at operating point [W]\n\nPower of the High Power Amplifier used as a last stage of '
                 'amplification in the satellite payload.'
                 'The value in watts is the value at operating point and for the carrier of interest.\n\n'
                 'Some satellites operate their HPAs at saturation in single carrier mode (typical DTH case).'
                 'Other satellites operate in multicarrier mode and reduced power (3dB Output Back Off is typical '
                 'for satellites serving VSATs)',
        '-iSBeam-':'Satellite Half Power Beam Diameter [\N{DEGREE SIGN}]\n\nBeam diameter expressed as an angle at '
                   'satellite level. The power radiated at the edge of this beam is half of the power radiated at '
                   'the peak of the beam (on-axis value).\n\n'
                   'The beam evaluated is a basic one with simple illumination of a parabolic reflector\n\n'
                   'Typical beam size : 0.4-1.4 degrees for GEO HTS satellites, 3..6 degrees for GEO DTH satellites.',
        '-iGOff-': 'Gain Offset from Peak [dB]\n\nThis offset allows to simulate terminals which are not all at '
                   'the beam peak. A 3 dB value would simulate a worst case position in a 3dB beam, typical approach '
                   'used in DTH. In single feed per beam HTS, a 1 dB value would give a typical median performance.'
                   'If you know the EIRP you have, the best is to iterate this value to get this EIRP '
                   '(the process will allow you to get a feeling of the tradeoff power / footprint size / EIRP. ',
        '-iPath-':'Path Length [km]\n\nDistance in kilometers from the satellite to the customer\'s terminal. '
                  'The actual distance depends on the orbit\'s altitude and on the positions of the satellite and '
                  'the terminal.\n\nMinimum distances : GEO : 36000 km, O3B : 8000 km, Starlink : 550 km,\n\nTypical '
                  'distances : GEO : 38000 km, O3B : 9000 km, Starlink : 700 km.',
        '-iLoss-':'Output Section Losses [dB]\n\nLoss of signal\'s power in the path connecting the HPA to the '
                  'antenna. This loss is associated with filters, waveguide sections, switches ...\n\n'
                  'Typical value : 2.5 dB for large classical satellites, 1 dB for active antennas with HPAs close to '
                  'the feeds. If the power value is given at antenna level, the value should just be set to zero.',
        '-iSCIR-':'Satellite C/I [dB]\n\n Signal impairment associated with satellite implementation,'
                  'expressed as a signal to noise ratio to be combined with the intrinsic Signal to Noise Ratio '
                  'affecting the link. Typical impairments are : intermodulation in the HPA, oscillator\'s phase'
                  'noise ...',
        '-iFade-':'Rain & Gaz Attenuation [dB]\n\nRain is affecting radio wave propagation, with a signal attenuating '
                  'increasing with the rain intensity and with the signal frequency. C band is almost unaffected, '
                  'Ku band is significantly affected, Ka band is severely affected, Q band is dramatically affected\n\n'
                  'Gazes composing the atmosphere are also causing attenuation even without rain, the corresponding '
                  'attenuation is typically 0.2 dB in Ku. The Rain & gaz attenuation depends on the actual geographical'
                  ' location and on actual weather events. By nature, it is is thus statistical (considering the past) '
                  'or probabilistic (considering the future).\n\nAll effects included, here are typical attenuation '
                  'figures exceeded for 0.1% of the time in Europe from the GEO orbit : Ku: 2.5 dB, Ka: 6.9 dB, 22 dB ',
        '-iOPow-':'Output Power [W]\n\nThe output power in watts at antenna output is associated with the useful '
                  'signal carrying user\'s information. It is also common to express this value in dBs (dBs transform '
                  'multiplications in additions, easier for human computation. Nevertheless, reasoning in watts tells '
                  'more about the physics.',
        '-iSGain-':'Satellite Antenna Gain \n\nAn antenna concentrating the signal in the direction of the users is '
                   'almost always required to compensate for the path loss associated with the distance from the '
                   'satellite to the terminal.\n\n The antenna gain is the ratio between the signal radiated '
                   'on the axis of the antenna (direction of maximum radiation) and the signal radiated by an '
                   'antenna radiating equally in all directions (for the same input power).\n\n'
                   'Antenna gains are without units but can be expressed in dB for convenience : dBi = dB relative to'
                   ' isotropic antenna (antenna radiating equally in all directions',
        '-iEIRP-':'Equivalent Isotropic Radiated Power\n\nThe product Power x Gain expressed in Watts is a convenient '
                  'characterisation of the satellite radiation capability. It does correspond to the power which would '
                  'be required for an isotropic antenna radiating in the same way in the direction of the antenna '
                  'considered.\n\nThere is no "power creation" of course : for the directive antenna, the integral of '
                  'the radiated signal over a sphere centered on the antenna is at best equal to the input power '
                  '(lossless antenna).\n\n'
                  'As the value in watts is usually pretty big, a value in dBW is more convenient '
                  'for practical human computations.',
        '-iPLoss-':'Path Dispersion Loss\n\nAssuming communication in free space (thus also in the vacuum), '
                   'this figure characterises the effect'
                   ' of the distance from the satellite to the terminal. It gives an attenuation equivalent to the '
                   'inverse ratio of the power reaching one square meter at the terminal side and the equivalent '
                   'isotropic radiated power at satellite level.\n\n'         
                   'This simply equals the surface in square meters of a sphere with a radius equal to the path length.'
                   'This attenuation is pretty big and is thus more humanly manageable in dB m\N{SUPERSCRIPT TWO}.\n\n'
                   'As the the vacuum is lossless, this "attenuation" is simply associated with the fact that only '
                   'a marginal fraction of the power radiated is captured in square meter at destination, '
                   'the rest is going somewhere else.',
        '-iPFD-':'Power Flux Density, Clear Sky\n\nSignal power per square meter at the terminal side. '
                 'The actual power captured by the terminal is given by this value multiplied by the effective surface '
                 'of the terminal\'s antenna.\n\nNote that if the surface of antenna is not perpendicular to the '
                 'propagation direction of the radio wave, the effective surface presented to the wave is reduced '
                 'and less power is captured.',
        '-iCPE-':'Customer Antenna Size [m]\n\nSize of the terminal antenna. A basic parabolic antenna with state of '
                 'the art efficiency is assumed.\n\n'
                 'The main source of noise is in general the terminal\'s radio front end'
                 ' attached to the antenna. A state of the art Noise Temperature of 80K is assumed for this front end.',
        '-iCPE_T-':'Noise Temperature [K]\n\nTotal Receiver\'s Clear Sky Noise Temperature. It includes all noise '
                   'temperature\'s contributors : receiver, sky, ground seen by the antenna... Antenna catalogs often '
                   'provide this value, the proposed default of 120K is a reasonable typical value. The computation '
                   'under rain fade conditions assumes 40K is affected by rain attenuation and the rest is not. ',
        '-iCGain-':'Customer Antenna Effective Area and G/T\n\nThe effective area in square meters is expressing the '
                   'capability of the terminal to capture the Power Flux Density '
                   '(the multiplication of both give the power captured). The effective area is typically 60% of the '
                   'physical surface of the antenna\'s aperture.'
                   'This capability can also be equivalently expressed as a gain as it\'s the case for the satellite '
                   'antenna.\n\nThe figure of merit of a receive antenna is best expressed as the G/T ratio, '
                   'ratio between antenna gain and the total Noise temperature in Kelvins. The noise is mainly coming '
                   'from the electronics of the radio front end, the ground seen by the antenna, the stars and the '
                   'atmospheric attenuator.\n\nIn case of rain, the signal is punished twice : the '
                   'attenuation makes it weaker and the rain attenuator generates noise added to the overall noise.\n\n'
                   'The noise power density N\N{SUBSCRIPT ZERO} is derived from the noise temperature with a very '
                   'simple formula : N\N{SUBSCRIPT ZERO}=kTB (k being the Boltzmann constant), '
                   'the G/T leads easily to the key overall link figure of merit C/N\N{SUBSCRIPT ZERO}.',
        '-iRXPow-':'RX Power at Antenna Output\n\nPower at receiver\'s antenna output before amplification. '
                   'This power is extremely small and can only be exploited after strong amplification.\n\n'
                   'As the main source of noise is in general coming from this amplification, the first amplification '
                   'stage has to be a Low Noise Amplifier. This power is "C" in the Shannon\'s equation.',
        '-iN0-' : 'Noise Power Density Antenna Output\n\nNoise Spectral Power Density of the radio front end under '
                  'actual link conditions (in Watts per MHz). '
                  'This PSD is N\N{SUBSCRIPT ZERO} in the Shannon\'s equation',
        '-iBRinf-':'Bit Rate at infinite Bandwidth\n\nBit Rate theoretically achievable when the signal occupies an '
                   'infinite Bandwidth, this value is a useful asymptotic limit. The corresponding value, deduced '
                   'from the Shannon\'s formula is given by 1.443 C/N\N{SUBSCRIPT ZERO}\n\nThis bit rate is an '
                   'asymptotic value and is thus never achieved in practice.',
        '-iBRhalf-':'Bit Rate at Spectral Efficiency=1/2\n\nBit Rate theoretically achievable at a Spectral Efficiency '
                    '= 1/2. The corresponding value, deduced from the Shannon\'s formula is given by 1.207 '
                    'C/N\N{SUBSCRIPT ZERO}\n\nThis operating point is bandwidth intensive ( bandwidth = 2 x bit rate). '
                    'Practical systems allow this operating point ( DVB-S2\'s QPSK 1/4 )',
        '-iBRUnit-':'Bit Rate at Spectral Efficiency=1\n\nBit Rate theoretically achievable at a Spectral Efficiency '
                    '= 1. The corresponding value, deduced from the Shannon\'s formula is given by '
                    'C/N\N{SUBSCRIPT ZERO}.\n\nThis data point has remarkable attributes : bandwidth = bit rate and '
                    'C/N = 1 or 0 dB, which means Noise Power = Signal Power.',
        '-iBRdouble-':'Bit Rate at Spectral Efficiency=2\n\nBit Rate theoretically achievable at a Spectral Efficiency '
                      '= 1. The corresponding value, deduced from the Shannon\'s formula is given by '
                      '0.667 C/N\N{SUBSCRIPT ZERO}.\n\nThis operating point is relatively bandwidth efficient '
                      '( bandwidth = 0.5 x bit rate) and is often considered as a typical setting.',
        '-iBW-':'Available Bandwidth [MHz]\n\nBandwith occupied by the communication channel. This bandwidth is usually'
                ' a degree of freedom of the system design, eventually constrained by technological constraints and '
                'various kind of frequency usage regulations. Interestingly this parameter is also often mentally '
                'constrained by past usages which were driven by technological constraints at that time.',
        '-iRO-':'Nyquist Filter Rolloff [%]\n\n'
                'To pass a limited bandwidth channel symbol have to be mapped on pulses, "filtered" to limit the '
                'Bandwidth occupied. Theoretically, filtering can be "brickwall", one symbol per second passing in '
                '1 Hertz. Practically, an excess of bandwidth is required, also called "Roll-Off of the filter.\n\n'
                'The filter used is designed to respect the symmetry condition expressed in the Nyquist Criterion '
                'avoiding inter-symbol interferences. Such a filter is called a Nyquist Filter. '
                'and the mimimum theoretical bandwidth (Roll-Off = zero) is called Nyquist Bandwidth.\n\n'
                'The Roll-Off or Excess of Bandwidth is usually expressed as a percentage of the Nyquist Bandwidth.',
        '-iCIR-':'Receiver\'s C/I [dB]\n\n Signal impairment associated with terminal implementation, expressed as a '
                'signal to noise ratio to be combined with the intrinsic Signal to Noise Ratio affecting the link.\n\n'
                'Impairments are multiple : Phase Noise of the radio front end, Quantization Noise of the receiver\'s '
                'Analog to Digital Conversion, effect of imperfect synchronisation ...\n\n'
                'Typical values of C/I corresponding to total implementation impairments range from 15 to 25 dB',
        '-iPenalty-':'Implementation Penalty vs theory [dB]\n\nTurbo and Turbo-like Codes are known for getting '
                     '"almost Shannon" performances. There are however still some implementation taxes '
                     ': codes always have a residual bit error rate, making it very low requires some CNR margin.\n\n'
                     'Other practical aspects also cost signal\'s energy like time and frequency synchronisation, '
                     'physical layer framing...\n\n DVB-S2x, using LDPC codes and modern modulation related features '
                     'is typically 1 dB away of the Shannon Limit in Quasi Error Free operation. Real systems also have'
                     ' to take margins, considering a reasonable value of 0.5 dB, a total penalty of 1.5 dB can be '
                     'considered as typical.\n\n'
                     'Original Turbo codes designed with higher residual bit error rates can get much closer '
                     'to the Shannon Limit. ',
        '-iOH-':'Higher Layers Overhead [%]\n\n The practical usage of information bits is based on a breakdown '
                'in multiple communications layers, all spending bits for the logistics of carrying user bits.'
                'For example, the process of encapsulation of IP datagrams on a DVB-S2x physical layer using'
                ' the GSE standard costs a few percents of net bit rate, spent in framing structures, integrity '
                'control bits ...\n\n'
                'In a modern efficient satellite forward communication system the overhead to IP costs typically 5%',
        '-iNBW-':'Nyquist Bandwidth\n\nThe modulated carrier is passing bits in groups mapped on modulation symbols.'
                'Satellite modulation schemes typically map from 1 to 8 bits on each symbol passing though the channel.'
                'The Bit Rate is directly linked to the symbol rate, the number of symbols per second passing '
                'the channel ( BR = SR . Number of Bits per Symbol ).\n\n'
                'To pass a bandwidth limited channel, symbols have to be mapped on pulses "filtered" to limit the '
                'bandwidth. Theoretically, filtering can be "brickwall", one symbol per second passing in 1 Hertz.'
                'Practically, an excess of bandwidth is required, also called "Roll-Off of the filter. '
                'The filter used is also designed to respect the symmetry condition expressed in the Nyquist Criterion '
                'avoiding inter-symbol interferences. Such a filter is thus called Nyquist Filter. '
                'and the minimum theoretical bandwidth (Roll-Off = zero) is called Nyquist Bandwidth.',
        '-iCNRbw-':'Signal to Noise Ratio in Available BW\n\n Ratio of the Signal Power and the Noise Power Captured '
                ' in the available bandwidth.',
        '-iCNRnyq-':'Signal to Noise Ratio in Nyquist BW\n\nRatio of the Signal Power and the Noise Power Captured '
                ' in the Nyquist Bandwidth = Available Bandwidth / ( 1 + Roll-Off).',
        '-iCNRrcv-':'Signal to Noise Ratio at Receiver Output\n\nRatio of the Signal Power and the total Noise Power'
                'captured along the complete communication chain (at receiver ouptut). This ratio is the relevant one'
                'for real-life performance evaluation. It is computed by combining the Signal to Noise in the Nyquist '
                'Bandwidth, the Receiver\'s C/I and the Satellite\'s C/I. Note that these 2 items are themselves '
                'resulting of many items.',
        '-iBRbw-':'Theoretical Bit Rate in Available BW\n\nBit Rate theoretically achieved with zero Roll-Off in '
                'the available bandwidth. This bit rate is given by a direct application of the Shannon Limit. '
                'The normalized bit rate expressed as a percentage of the bit rate at infinite bandwidth is also given '
                'as well as the spectral efficiency of the available bandwidth.',
        '-iBRnyq-':'Theoretical Bit Rate in Nyquist BW\n\nBit Rate theoretically achieved in '
                'the Nyquist bandwidth (after having removed the Nyquist Roll-Off from the available Bandwidth).'
                'This bit rate is given by a direct application of the Shannon Limit. The normalized bit rate '
                'expressed as a percentage of the bit rate at infinite bandwidth is also given as well as the spectral '
                'efficiency of the available bandwidth.The efficiency in bit per symbol is also given and does '
                'correspond to the classical spectral efficiency in the Nyquist bandwidth.',
        '-iBRrcv-':'Practical Physcial Layer Bit Rate\n\n Practical Bit Rate achieved using real-world conditions. '
                    'This bit rate is evaluated by using the "all degradations included" signal to noise ratio'
                    'in the Shannon\'s formula.'
                    'This bit rate does correspond to the user bits of the Physical Layer Frames.',
        '-iBRhigh-':'Practical Higher Layers Bit Rate\n\nPractical Bit Rate achieved using real-world modulation '
                    'and coding and modern encapsulation methods of higher layers strcutures.\n\n This Bit Rate does '
                    'typically correspond to the user bits of the IP datagrams',
        '-Satellite-':'The evaluation is decomposed in 3 sections:\n\n'
                      '1. The satellite link : satellite transmitter and path to the receiver\'s location with '
                      'associated key characteristics \n\n'
                      '2. The radio front end : antenna and amplification unit capturing as much signal as possible '
                      'and as little noise as possible\n\n'
                      '3. The base-band processing unit : unit extracting from a modulated carrier the useful '
                      'information bits.'
                      'As of today, all key functions are performed via digital signal processing : Nyquist filtering, '
                      'synchronisation, demodulation, error correction, higher layer "decapsulation"...\n\n'
                      'All fields are initially filled with meaningful values, you should start the exploration by '
                      'changing the straightforward parameters and keep the intimidating figures unchanged. '
                      'All parameters are "clickable" for getting associated background information.',
        'Advanced': 'The Shannon Limit is  a very powerful tool to analyse communication systems\' design, trade offs.'
                    'All capacity evaluations in this tool are based on direct application of this formula taking '
                    'into account real world impairments via signal to noise combinations. With this approach, '
                    'using the overall C/N evaluated for a practical communication link gives a good estimate of the '
                    'capacity achievable.\n\nApplying in addition the known average penalty of real modulation and '
                    'coding schemes makes it accurate enough for initial systems evaluations.\n\nThe analytic formulas '
                    'derived from the Shannon Limit for given spectral efficiencies are also of great help to drive '
                    'the thinking in practical trade-offs.\n\n'
                    'Additional useful links for people interested in a theoretical immersion :'
                    'https://en.wikipedia.org/wiki/Nyquist_ISI_criterion\n'
                    'https://en.wikipedia.org/wiki/Error_correction_code#Forward_error_correction\n'
                    'https://en.wikipedia.org/wiki/Viterbi_decoder\n'
                    'https://en.wikipedia.org/wiki/Turbo_code\n'
                    'https://en.wikipedia.org/wiki/DVB-S2\n'
                    'https://en.wikipedia.org/wiki/OSI_model\n',
        'Help':'Recommendations for using the tool\n\nThe first purpose of the tool is educational, allowing people to '
               'better understand the physics of communications and the role of key parameters\n\n'
               'All labels can be \"clicked\" to get information about associated item. All values '
               '(including this text) can be copy/pasted for further usage.\n\n'
               'The user should try multiple values in the fields one per one (starting from the least intimidating), '
               'explore the graphs and try to understand the underlying physics.\n\n'
               'The units for the different figures are as explicit as possible to facilitate the exploration.\n\n'
               'Despite the simplicity of the approach, the tool can also be useful to do a quick analysis of a '
               'communication link with a first order approach, avoiding the trap of the illusion of precision.\n\n'

        }


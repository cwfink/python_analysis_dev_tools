import numpy as np
import matplotlib.pyplot as plt


def plot_full_trace(didv, poles="all", plotpriors = True, lgcsave = False, savepath = "", savename = ""):
    """
    Function to plot the entire trace in time domain
    
    Parameters
    ----------
        didv : class
            The DIDV class object that the data is stored in
        poles : int, string, array_like, optional
            The pole fits that we want to plot. If set to "all", then plots
            all of the fits. Can also be set to just one of the fits. Can be set
            as an array of different fits, e.g. [1, 2]
        plotpriors : boolean, optional
            Boolean value on whether or not the priors fit should be plotted.
        lgcsave : boolean, optional
            Boolean value on whether or not the figure should be saved
        savepath : string, optional
            Where the figure should be saved. Saved in the current directory
            by default.
        savename : string, optional
            A string to append to the end of the file name if saving. Empty string
            by default.
    """

    if poles == "all":
        poleslist = np.array([1,2,3])
    else:
        poleslist = np.array(poles)

    ## plot the entire trace with fits
    fig,ax=plt.subplots(figsize=(10,6))
    ax.plot(didv.time*1e6, didv.tmean*1e6 - didv.offset*1e6, color='black', label='mean')

    if (didv.fitparams1 is not None) and (1 in poleslist):
        ax.plot(didv.time*1e6+didv.fitparams1[2]*1e6, (didv.didvfit1_timedomain-didv.offset)*1e6, 
                color='magenta', alpha=0.9, label='1-pole fit')
        
    if (didv.fitparams2 is not None) and (2 in poleslist):
        ax.plot(didv.time*1e6+didv.fitparams2[4]*1e6, (didv.didvfit2_timedomain-didv.offset)*1e6, 
                color='green', alpha=0.9, label='2-pole fit')
        
    if (didv.fitparams3 is not None) and (3 in poleslist):
        ax.plot(didv.time*1e6+didv.fitparams3[6]*1e6, (didv.didvfit3_timedomain-didv.offset)*1e6, 
                color='orange', alpha=0.9, label='3-pole fit')
        
    if (didv.irwinparams2priors is not None) and (plotpriors):
        ax.plot(didv.time*1e6+didv.irwinparams2priors[6]*1e6, (didv.didvfit2priors_timedomain-didv.offset)*1e6, 
                color='cyan', alpha=0.9, label='2-pole fit with priors')

    ax.set_xlabel('Time ($\mu$s)')
    ax.set_ylabel('Amplitude ($\mu$A)')
    ax.set_xlim([didv.time[0]*1e6, didv.time[-1]*1e6])
    ax.legend(loc='upper left')
    ax.set_title("Full Trace of dIdV")
    ax.grid(linestyle='dotted')
    ax.tick_params(which='both',direction='in',right=True,top=True)

    if lgcsave:
        fig.savefig(savepath+f"full_trace_{savename}.png")
        plt.close(fig)
    else:
        plt.show()

def plot_single_period_of_trace(didv, poles="all", plotpriors = True, lgcsave = False, savepath = "", savename = ""):
    """
    Function to plot a single period of the trace in time domain
    
    Parameters
    ----------
        didv : class
            The DIDV class object that the data is stored in
        poles : int, string, array_like, optional
            The pole fits that we want to plot. If set to "all", then plots
            all of the fits. Can also be set to just one of the fits. Can be set
            as an array of different fits, e.g. [1, 2]
        plotpriors : boolean, optional
            Boolean value on whether or not the priors fit should be plotted.
        lgcsave : boolean, optional
            Boolean value on whether or not the figure should be saved
        savepath : string, optional
            Where the figure should be saved. Saved in the current directory
            by default.
        savename : string, optional
            A string to append to the end of the file name if saving. Empty string
            by default.
    """

    if poles == "all":
        poleslist = np.array([1,2,3])
    else:
        poleslist = np.array(poles)

    period = 1.0/didv.sgfreq
        
    ## plot a single period of the trace
    fig,ax=plt.subplots(figsize=(10,6))
    ax.plot(didv.time*1e6+dtfit*1e6, didv.tmean*1e6 - didv.offset*1e6, color='black', label='mean')

    if (didv.fitparams1 is not None) and (1 in poleslist):
        ax.plot(didv.time*1e6+didv.fitparams1[2]*1e6, (didv.didvfit1_timedomain-didv.offset)*1e6, 
                color='magenta', alpha=0.9, label='1-pole fit')
        
    if (didv.fitparams2 is not None) and (2 in poleslist):
        ax.plot(didv.time*1e6+didv.fitparams2[4]*1e6, (didv.didvfit2_timedomain-didv.offset)*1e6, 
                color='green', alpha=0.9, label='2-pole fit')
        
    if (didv.fitparams3 is not None) and (3 in poleslist):
        ax.plot(didv.time*1e6+didv.fitparams3[6]*1e6, (didv.didvfit3_timedomain-didv.offset)*1e6, 
                color='orange', alpha=0.9, label='3-pole fit')
        
    if (didv.irwinparams2priors is not None) and (plotpriors):
        ax.plot(didv.time*1e6+didv.irwinparams2priors[6]*1e6, (didv.didvfit2priors_timedomain-didv.offset)*1e6, 
                color='cyan', alpha=0.9, label='2-pole fit with priors')

    ax.set_xlabel('Time ($\mu$s)')
    ax.set_ylabel('Amplitude ($\mu$A)')
    ax.set_xlim([didv.time[0]*1e6, didv.time[0]*1e6+period*1e6])
    ax.legend(loc='upper left')
    ax.set_title("Single Period of Trace")
    ax.grid(linestyle='dotted')
    ax.tick_params(which='both',direction='in',right=True,top=True)

    if lgcsave:
        fig.savefig(savepath+f"trace_one_period_{savename}.png")
        plt.close(fig)
    else:
        plt.show()

def plot_zoomed_in_trace(didv, poles="all", zoomfactor=0.1, plotpriors = True, lgcsave = False, savepath = "", savename = ""):
    """
    Function to plot a zoomed in portion of the trace in time domain. This plot zooms in on the
    overshoot of the didv.
    
    Parameters
    ----------
        didv : class
            The DIDV class object that the data is stored in
        poles : int, string, array_like, optional
            The pole fits that we want to plot. If set to "all", then plots
            all of the fits. Can also be set to just one of the fits. Can be set
            as an array of different fits, e.g. [1, 2]
        zoomfactor : float, optional, optional
            Number between zero and 1 to show different amounts of the zoomed in trace.
        plotpriors : boolean, optional
            Boolean value on whether or not the priors fit should be plotted.
        lgcsave : boolean, optional
            Boolean value on whether or not the figure should be saved
        savepath : string, optional
            Where the figure should be saved. Saved in the current directory
            by default.
        savename : string, optional
            A string to append to the end of the file name if saving. Empty string
            by default.
    """

    if poles == "all":
        poleslist = np.array([1,2,3])
    else:
        poleslist = np.array(poles)
        
    period = 1.0/didv.sgfreq

    ## plot zoomed in on the trace
    fig,ax=plt.subplots(figsize=(10,6))
    ax.plot(didv.time*1e6, didv.tmean*1e6 - didv.offset*1e6, color='black', label='mean')

    if (didv.fitparams1 is not None) and (1 in poleslist):
        ax.plot(didv.time*1e6+didv.fitparams1[2]*1e6, (didv.didvfit1_timedomain-didv.offset)*1e6, 
                color='magenta', alpha=0.9, label='1-pole fit')
        
    if (didv.fitparams2 is not None) and (2 in poleslist):
        ax.plot(didv.time*1e6+didv.fitparams2[4]*1e6, (didv.didvfit2_timedomain-didv.offset)*1e6, 
                color='green', alpha=0.9, label='2-pole fit')
        
    if (didv.fitparams3 is not None) and (3 in poleslist):
        ax.plot(didv.time*1e6+didv.fitparams3[6]*1e6, (didv.didvfit3_timedomain-didv.offset)*1e6, 
                color='orange', alpha=0.9, label='3-pole fit')
        
    if (didv.irwinparams2priors is not None) and (plotpriors):
        ax.plot(didv.time*1e6+didv.irwinparams2priors[6]*1e6, (didv.didvfit2priors_timedomain-didv.offset)*1e6, 
                color='cyan', alpha=0.9, label='2-pole fit with priors')

    ax.set_xlabel('Time ($\mu$s)')
    ax.set_ylabel('Amplitude ($\mu$A)')

    ax.set_xlim([(0.5-zoomfactor/2)*period*1e6, (0.5+zoomfactor/2)*period*1e6])

    ax.legend(loc='upper left')
    ax.set_title("Zoomed In Portion of Trace")
    ax.grid(linestyle='dotted')
    ax.tick_params(which='both',direction='in',right=True,top=True)
    if lgcsave:
        fig.savefig(savepath+f"zoomed_in_trace_{savename}.png")
        plt.close(fig)
    else:
        plt.show()

def plot_didv_flipped(didv, poles="all", plotpriors = True, lgcsave = False, savepath = "", savename = ""):
    """
    Function to plot the flipped trace in time domain. This function should be used to 
    test if there are nonlinearities in the didv
    
    Parameters
    ----------
        didv : class
            The DIDV class object that the data is stored in
        poles : int, string, array_like, optional
            The pole fits that we want to plot. If set to "all", then plots
            all of the fits. Can also be set to just one of the fits. Can be set
            as an array of different fits, e.g. [1, 2]
        plotpriors : boolean, optional
            Boolean value on whether or not the priors fit should be plotted.
        lgcsave : boolean, optional
            Boolean value on whether or not the figure should be saved
        savepath : string, optional
            Where the figure should be saved. Saved in the current directory
            by default.
        savename : string, optional
            A string to append to the end of the file name if saving. Empty string
            by default.
    """

    if poles == "all":
        poleslist = np.array([1,2,3])
    else:
        poleslist = np.array(poles)

    ## plot the traces as well as the traces flipped in order to check asymmetry
    fig,ax=plt.subplots(figsize=(10,6))
    ax.plot(didv.time*1e6,(didv.tmean-didv.offset)*1e6,color='black',label='data')

    period = 1.0/didv.sgfreq
    time_flipped=didv.time-period/2.0
    tmean_flipped=-(didv.tmean-didv.offset)
    ax.plot(time_flipped*1e6,tmean_flipped*1e6,color='blue',label='flipped data')

    if (didv.fitparams1 is not None) and (1 in poleslist):
        ax.plot(didv.time*1e6+didv.fitparams1[2]*1e6, (didv.didvfit1_timedomain-didv.offset)*1e6, 
                color='magenta', alpha=0.9, label='1-pole fit')
        
    if (didv.fitparams2 is not None) and (2 in poleslist):
        ax.plot(didv.time*1e6+didv.fitparams2[4]*1e6, (didv.didvfit2_timedomain-didv.offset)*1e6, 
                color='green', alpha=0.9, label='2-pole fit')
        
    if (didv.fitparams3 is not None) and (3 in poleslist):
        ax.plot(didv.time*1e6+didv.fitparams3[6]*1e6, (didv.didvfit3_timedomain-didv.offset)*1e6, 
                color='orange', alpha=0.9, label='3-pole fit')
        
    if (didv.irwinparams2priors is not None) and (plotpriors):
        ax.plot(didv.time*1e6+didv.irwinparams2priors[6]*1e6, (didv.didvfit2priors_timedomain-didv.offset)*1e6, 
                color='cyan', alpha=0.9, label='2-pole fit with priors')

    ax.set_xlabel('Time ($\mu$s)')
    ax.set_ylabel('Amplitude ($\mu$A)')
    ax.legend(loc='upper left')
    ax.set_title("Flipped Traces to Check Asymmetry")
    ax.grid(linestyle='dotted')
    ax.tick_params(which='both',direction='in',right=True,top=True)
    if lgcsave:
        fig.savefig(savepath+f"flipped_trace_{savename}.png")
        plt.close(fig)
    else:
        plt.show()

def plot_re_im_didv(didv, poles="all", plotpriors = True, lgcsave = False, savepath = "", savename = ""):
    """
    Function to plot the real and imaginary parts of the didv in frequency space.
    Currently creates two different plots.
    
    Parameters
    ----------
        didv : class
            The DIDV class object that the data is stored in
        poles : int, string, array_like, optional
            The pole fits that we want to plot. If set to "all", then plots
            all of the fits. Can also be set to just one of the fits. Can be set
            as an array of different fits, e.g. [1, 2]
        plotpriors : boolean, optional
            Boolean value on whether or not the priors fit should be plotted.
        lgcsave : boolean, optional
            Boolean value on whether or not the figure should be saved
        savepath : string, optional
            Where the figure should be saved. Saved in the current directory
            by default.
        savename : string, optional
            A string to append to the end of the file name if saving. Empty string
            by default.
    """

    if poles == "all":
        poleslist = np.array([1,2,3])
    else:
        poleslist = np.array(poles)

    goodinds=np.abs(didv.didvmean/didv.didvstd) > 2.0 ## don't plot points with huge errors
    fitinds = didv.freq>0
    plotinds= np.logical_and(fitinds, goodinds)
    

    ## plot the real part of the dIdV in frequency domain
    fig,ax=plt.subplots(figsize=(10,6))

    ax.scatter(didv.freq[plotinds],np.real(didv.didvmean)[plotinds],color='blue',label='mean',s=5)
    ## plot error in real part of dIdV
    ax.plot(didv.freq[plotinds],np.real(didv.didvmean+didv.didvstd)[plotinds],color='black',label='1-$\sigma$ bounds',alpha=0.1)
    ax.plot(didv.freq[plotinds],np.real(didv.didvmean-didv.didvstd)[plotinds],color='black',alpha=0.1)

    if (didv.fitparams1 is not None) and (1 in poleslist):
        ax.plot(didv.freq[fitinds],np.real(didv.didvfit1_freqdomain)[fitinds],
                color='magenta',label='1-pole fit')
        
    if (didv.fitparams2 is not None) and (2 in poleslist):
        ax.plot(didv.freq[fitinds],np.real(didv.didvfit2_freqdomain)[fitinds],
                color='green',label='2-pole fit')
        
    if (didv.fitparams3 is not None) and (3 in poleslist):
        ax.plot(didv.freq[fitinds],np.real(didv.didvfit3_freqdomain)[fitinds],
                color='orange',label='3-pole fit')
        
    if (didv.irwinparams2priors is not None) and (plotpriors):
        ax.plot(didv.freq[fitinds],np.real(didv.didvfit2priors_freqdomain)[fitinds],
                color='cyan',label='2-pole fit with priors')


    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Re($dI/dV$) ($\Omega^{-1}$)')
    ax.set_xscale('log')
    
    yhigh = max(np.real(didv.didvmean)[plotinds][didv.freq[plotinds]<1e5])
    ylow = min(np.real(didv.didvmean)[plotinds][didv.freq[plotinds]<1e5])
    ybnd = np.max([yhigh,-ylow])
    
    ax.set_ylim([-ybnd, ybnd])
    ax.set_xlim([min(didv.freq[fitinds]), max(didv.freq[fitinds])])
    ax.legend(loc='upper left')
    ax.set_title("Real Part of dIdV")
    ax.tick_params(right=True,top=True)
    ax.grid(which='major')
    ax.grid(which='minor',linestyle='dotted',alpha=0.3)

    if lgcsave:
        fig.savefig(savepath+f"didv_real_{savename}.png")
        plt.close(fig)
    else:
        plt.show()

    ## plot the imaginary part of the dIdV in frequency domain
    fig,ax=plt.subplots(figsize=(10,6))

    ax.scatter(didv.freq[plotinds],np.imag(didv.didvmean)[plotinds],color='blue',label='x(f) mean',s=5)

    ## plot error in imaginary part of dIdV
    ax.plot(didv.freq[plotinds],np.imag(didv.didvmean+didv.didvstd)[plotinds],color='black',label='x(f) 1-$\sigma$ bounds',alpha=0.1)
    ax.plot(didv.freq[plotinds],np.imag(didv.didvmean-didv.didvstd)[plotinds],color='black',alpha=0.1)

    if (didv.fitparams1 is not None) and (1 in poleslist):
        ax.plot(didv.freq[fitinds],np.imag(didv.didvfit1_freqdomain)[fitinds],
                color='magenta',label='1-pole fit')
        
    if (didv.fitparams2 is not None) and (2 in poleslist):
        ax.plot(didv.freq[fitinds],np.imag(didv.didvfit2_freqdomain)[fitinds],
                color='green',label='2-pole fit')
        
    if (didv.fitparams3 is not None) and (3 in poleslist):
        ax.plot(didv.freq[fitinds],np.imag(didv.didvfit3_freqdomain)[fitinds],
                color='orange',label='3-pole fit')
        
    if (didv.irwinparams2priors is not None) and (plotpriors):
        ax.plot(didv.freq[fitinds],np.imag(didv.didvfit2priors_freqdomain)[fitinds],
                color='cyan',label='2-pole fit with priors')

    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Im($dI/dV$) ($\Omega^{-1}$)')
    ax.set_xscale('log')
    
    yhigh = max(np.imag(didv.didvmean)[plotinds][didv.freq[plotinds]<1e5])
    ylow = min(np.imag(didv.didvmean)[plotinds][didv.freq[plotinds]<1e5])
    ybnd = np.max([yhigh,-ylow])
    
    ax.set_ylim([-ybnd,ybnd])
    ax.set_xlim([min(didv.freq[fitinds]), max(didv.freq[fitinds])])
    ax.legend(loc='upper left')
    ax.set_title("Imaginary Part of dIdV")
    ax.tick_params(which='both',direction='in',right=True,top=True)
    ax.grid(which='major')
    ax.grid(which='minor',linestyle='dotted',alpha=0.3)

    if lgcsave:
        fig.savefig(savepath+f"didv_imag_{savename}.png")
        plt.close(fig)
    else:
        plt.show()
        
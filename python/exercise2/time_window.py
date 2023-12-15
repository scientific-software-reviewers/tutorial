from datetime import datetime, timedelta

class TimeWindow:
    """ Observations for a TIEGCM experiment """
    
    def __init__(self, start_time, end_time, delta):
        """ Initialize the window and model times associated with a TIEGCM experiment
        
        start_time - string '%Y-%m-%d %H:%M:%S' model inital time
        end_time   - string '%Y-%m-%d %H:%M:%S' model end time
        delta - integer  assimilation window time in hours
        
        model_time is the center of the window.
        
        observation_time_window = model_time +/- 0.5*delta
        
        The assimilation window has to be non-overlapping,
        so start the window at +1 second and end on
        exactly the time boundary.
                
        """
        
        # Error checking of delta input
        if delta > 23:
          raise ValueError("invalid delta {} should be [0-23] hours".format(delta))

        if delta < 0:
          raise ValueError("invalid delta {} should be [0-23] hours".format(delta))

        if delta == 0:
          raise ValueError("invalid delta {} cannot be exactly 0 hours".format(delta))


        self.start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        self.end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        self.delta = delta
        self.delta_half = delta / 2
            
        # create a list of times for the experiment
        #   (model_end_time + 0.5*delta) - (model_start_time - 0.5*delta)
        num_windows = int( (self.end_time - self.start_time + timedelta(hours=self.delta)).total_seconds() / timedelta(hours=self.delta).total_seconds() )

        self.window_start_times = [ self.start_time-timedelta(hours=self.delta_half)+x*timedelta(hours=self.delta) for x in range(num_windows)]
        
        self.window_end_times = [x+timedelta(hours=self.delta) for x in self.window_start_times]
        self.model_end_times = [x+timedelta(hours=self.delta_half)+timedelta(hours=self.delta) for x in self.window_start_times]
        
        self.window_start_times = [ x+timedelta(seconds=1) for x in self.window_start_times] # +1 second to window start
        self.model_times = [x+timedelta(hours=self.delta_half) for x in self.window_start_times]  # model start time has +1 second also

        self.num_cycles = len(self.model_times)

    def info(self):

        """ prints first and last window times """

        print("win num_cycles", self.num_cycles)

        if self.num_cycles > 0:

            print("--- first window ---")
            print("win start        ", self.window_start_times[0])
            print("win end          ", self.window_end_times[0])
            print("model start time ", self.model_times[0])
            print("model end time   ", self.model_end_times[0])
            
            print("--- last window ---")
            print("win start        ", self.window_start_times[-1])
            print("win end          ", self.window_end_times[-1])
            print("model start time ", self.model_times[-1])
            print("model end time   ", self.model_end_times[-1])
        

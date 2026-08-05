from datetime import datetime, timedelta


class TimeWindow:
    """
    Calculates the hour-long model stop times ("model times") between a
    start and final time, and the +/- 30 minute observation window
    ("window times") around each model stop.

    Parameters
    ----------
    start_time : datetime
        Time of the first experiment.
    final_time : datetime
        Time of the last experiment. Must be after start_time.
    delta : timedelta
        Duration between experiments (e.g. timedelta(hours=1)).
        Must be a positive, non-zero duration.
    window_halfwidth : timedelta, optional
        Half-width of the observation window around each model stop.
        Defaults to timedelta(minutes=30).
    """

    def __init__(self, start_time, final_time, delta,
                 window_halfwidth=timedelta(minutes=30)):

        # --- Type checks -------------------------------------------------
        if not isinstance(start_time, datetime):
            raise TypeError("start_time must be a datetime object")
        if not isinstance(final_time, datetime):
            raise TypeError("final_time must be a datetime object")
        if not isinstance(delta, timedelta):
            raise TypeError("delta must be a timedelta object")
        if not isinstance(window_halfwidth, timedelta):
            raise TypeError("window_halfwidth must be a timedelta object")

        # --- Value checks (this is where the bug lived) -------------------
        # delta must be strictly positive, otherwise the number of
        # experiments still "counts" fine (abs value / floor division can
        # look reasonable) but every window/model time after the first is
        # computed by walking *backwards* instead of forwards.
        if delta <= timedelta(0):
            raise ValueError(
                f"delta must be a positive, non-zero timedelta, got {delta}"
            )

        # final_time must actually be after start_time, or we again get
        # a nonsensical (or negative) number of experiments.
        if final_time <= start_time:
            raise ValueError(
                "final_time must be after start_time "
                f"(got start_time={start_time}, final_time={final_time})"
            )

        # delta should not be longer than the total experiment period,
        # otherwise there are zero experiments, which is probably not
        # what the user intended.
        total_duration = final_time - start_time
        if delta > total_duration:
            raise ValueError(
                f"delta ({delta}) is larger than the total time between "
                f"start_time and final_time ({total_duration})"
            )

        # window_halfwidth must be positive too, and — since the model
        # is stopped every `delta` — it probably shouldn't be larger
        # than half of delta, or windows would overlap.
        if window_halfwidth <= timedelta(0):
            raise ValueError(
                "window_halfwidth must be a positive, non-zero timedelta, "
                f"got {window_halfwidth}"
            )
        if window_halfwidth * 2 > delta:
            raise ValueError(
                f"window_halfwidth ({window_halfwidth}) is too large for "
                f"delta ({delta}); observation windows would overlap"
            )

        self.start_time = start_time
        self.final_time = final_time
        self.delta = delta
        self.window_halfwidth = window_halfwidth

        # Number of hour-long experiments between start and final time.
        self.n_experiments = int(total_duration / delta)

        self._compute_times()

    def _compute_times(self):
        """Compute the list of model stop times and their windows."""
        self.model_times = [
            self.start_time + i * self.delta
            for i in range(self.n_experiments + 1)
        ]
        self.window_starts = [
            t - self.window_halfwidth for t in self.model_times
        ]
        self.window_ends = [
            t + self.window_halfwidth for t in self.model_times
        ]

    def __repr__(self):
        return (
            f"TimeWindow(start_time={self.start_time!r}, "
            f"final_time={self.final_time!r}, delta={self.delta!r}, "
            f"n_experiments={self.n_experiments})"
        )
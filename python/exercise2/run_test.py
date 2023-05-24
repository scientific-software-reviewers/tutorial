from time_window import TimeWindow

initial_time = '2002-03-21 00:00:00'
end_time = '2002-03-28 02:00:00'
delta = -1 

print('initial time = ', initial_time)
print('    end time = ', end_time)

win = TimeWindow(initial_time, end_time, delta)

win.info()

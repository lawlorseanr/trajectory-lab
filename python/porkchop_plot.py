"""Toy porkchop grid — fictional Earth-Mars transfer."""
def grid(c3_values, tof_days):
    return {(c3, tof): c3 * 0.01 * tof for c3 in c3_values for tof in tof_days}

# note update 33

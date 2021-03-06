import pygtfs
sched = pygtfs.Schedule(":memory:")
pygtfs.append_feed(sched, "../subway_gtfs")
pair_set = set()
with open('subway_pair_traveltime.csv','a') as file:
    for tr in sched.trips:
        n = len(tr.stop_times)
        r_id = tr.route_id
        sts = [(st.stop_id, st.arrival_time, st.departure_time)for st in tr.stop_times]
        sts.sort(key=lambda x:x[1])
        for i in range(n - 1):
            j = i + 1
            s_id = sts[i][0]
            e_id = sts[j][0]
            if not (r_id,s_id,e_id) in pair_set:
                start = sts[i][1]
                end = sts[j][2]
                pair_set.add((r_id,s_id,e_id))
#                 print(s_id,e_id,str(end-start))
                file.write(tr.route_id+','+s_id+','+e_id+','+str(end-start))
                file.write('\n')

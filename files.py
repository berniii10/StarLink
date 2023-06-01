path = "data/"
pings_path = "data/pings/"
speedtest_path = "data/speedtests/"

ping = path + "ping.csv"
ping_header = ["date", "host_name", "host_ip", "time"]

speedtest = path + "speedtest.csv"
speedtest_header = ["date", "ping", "upload", "download"]

traceroute = path + "traceroute.csv"
traceroute_header = ["date", "host", "ip", "max_hops", "hops"]


ping_test = path + "pingtests.csv"
ping_test_header = ["date", "host", "ip", "icmp", "ttl", "rtt", "trans_pack", "recv_pack", "pack_loss", "min/avg/max/mdev"]

speed_test = path + "speedtests.csv"
speed_test_header = ["date", "ping", "upload", "download"]



pings_log = path + "pingslog.csv"
speedtests_log = path + "speedtests_log.csv"
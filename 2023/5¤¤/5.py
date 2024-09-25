def oppg1(filename):

    with open(filename) as f:
        seeds = list(map(int,f.readline().split()[1:]))

        almanac = {}

        current_source = ''

        for line in f.readlines():
            if line[0].isalpha():
                source,destination = line.split()[0].split('-to-')
                current_source = source
                almanac[source] = {'destination':destination, 'ranges':[]}
            elif line[0].isdigit():
                almanac[source]['ranges'].append(tuple(map(int,line.split())))
    
    current_state = 'seed'

    while current_state != 'location':
        ranges = almanac[current_state]['ranges']

        for i in range(len(seeds)):
            for dest_num,source_num,step in ranges:
                if source_num <= seeds[i] <= source_num + step:
                    seeds[i] = seeds[i] + (dest_num-source_num)
                    break
    
        current_state = almanac[current_state]['destination']

    print(min(seeds))
    

def oppg2(filename):

    with open(filename) as f:
        seed_line = list(map(int,f.readline().split()[1:]))
        seed_ranges = []

        for i in range(0,len(seed_line),2):
            seed_ranges.append((seed_line[i], seed_line[i]+seed_line[i+1]-1))

        almanac = {}

        for line in f.readlines():
            if line[0].isalpha():
                source,destination = line.split()[0].split('-to-')
                almanac[source] = {'destination':destination, 'ranges':[]}
            elif line[0].isdigit():
                dest_start,source_start, range_length = map(int,line.split())
                almanac[source]['ranges'].append((source_start,source_start+range_length,dest_start-source_start))

    current_state = 'seed'

    while current_state != 'location':
        new_seed_ranges = []

        while seed_ranges:
            seed_range_start,seed_range_stop = seed_ranges.pop()

            match_found = False

            for range_start,range_stop,conversion in almanac[current_state]['ranges']:
                if seed_range_start >= range_start and seed_range_stop <= range_stop:
                    new_seed_ranges.append((seed_range_start+conversion,seed_range_stop+conversion))
                    match_found = True
                elif seed_range_start >= range_start and seed_range_start <= range_stop:
                    new_seed_ranges.append((seed_range_start+conversion,range_stop+conversion))
                    seed_ranges.append((range_stop+1,seed_range_stop))
                    match_found = True
                elif seed_range_stop <= range_stop and seed_range_stop >= range_start:
                    new_seed_ranges.append((range_start+conversion,seed_range_stop+conversion))
                    seed_ranges.append((seed_range_start,range_start-1))
                    match_found = True

            if not match_found:
                new_seed_ranges.append((seed_range_start,seed_range_stop))

        seed_ranges = new_seed_ranges

        current_state = almanac[current_state]['destination']
    
    print(min(seed_range[0] for seed_range in seed_ranges))


oppg2('5-input.txt')
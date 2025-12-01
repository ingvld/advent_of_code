import sys

with open(sys.argv[1]) as f:
    msg = bin(int(f.read().strip(),16))[2:]

def consume_real_value(msg, version_sum):
    if msg[0] == '0':
        return msg[4:], version_sum
    return consume_real_value(msg[4:],version_sum)

def consume_packet(msg,version_sum):
    if not msg:
        return msg, version_sum
    version_sum += int(msg[:3])
    
    if msg[3:6] == '100':
        return consume_real_value(msg[6:], version_sum)
   
    if msg[7] == '0':
        subpackets_length = int(msg[8:23],2)
        sub_msg, sub_sum = msg[23:23+subpackets_length], 0

        while sub_msg:
            sub_msg, sub_sum = consume_packet(sub_msg,sub_sum)

        return msg[23+subpackets_length:], sum+sub_sum

    nr_of_subpackets = int(msg[8:19],2)
    for i in range(nr_of_subpackets):
        msg, version_sum = consume_packet(msg[19:], version_sum)
    
    return msg,version_sum

print(consume_packet(msg,0))

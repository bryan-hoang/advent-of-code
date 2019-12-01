import re

raw_claims = [line for line in open('input')]

# parse

parsed_claims = []

for raw_claim in raw_claims:
    parsed_claims.append(map(int, re.findall('#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)', raw_claim)[0]))
    # alternate method: x = ''.join(c if c.isnumeric() else ' ' for c in claim).split(' ')

claimed_points = set()
intersected_claims = set()

for claim in parsed_claims:
    for x in range(claim[1], claim[1] + claim[3]):
        for y in range(claim[2], claim[2] + claim[4]):
            if (x, y) not in claimed_points:
                claimed_points.add((x, y))
            else:
                intersected_claims.add((x, y))

print('%d square inches of fabric are within two or more claims!' %
      len(intersected_claims))

for claim in parsed_claims:
    for x in range(claim[1], claim[1] + claim[3]):
        for y in range(claim[2], claim[2] + claim[4]):
            if (x, y) in intersected_claims:
                break
        else:
            continue
        break
    else:
        print('The ID of the only claim that doesn\'t overlap is %d!' % claim[0])

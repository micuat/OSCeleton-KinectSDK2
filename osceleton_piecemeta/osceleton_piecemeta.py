import csv

filename = 'points-MSK2-1503685970755.14.csv'
joints = {}
with open(filename, newline='') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
  for row in csvreader:
    if row[0] == 'Joint':
      joint = int(row[3]) - 1
      x = row[4]
      y = row[5]
      z = row[6]
      timestamp = row[8]
      if timestamp not in joints:
        joints[timestamp] = []
      while len(joints[timestamp]) <= joint:
        joints[timestamp].append({'x': float('nan'), 'y': float('nan'), 'z': float('nan')})
      joints[timestamp][joint]['x'] = x
      joints[timestamp][joint]['y'] = y
      joints[timestamp][joint]['z'] = z
#      print('/'.join(row))
print(joints)


with open('pm-' + filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\t',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    head = []
    head.append('timestamp')
    count = 0
    for timestamp in joints:
      for data in joints[timestamp]:
        head.append(str(count) + '/x')
        head.append(str(count) + '/y')
        head.append(str(count) + '/z')
        count += 1
      csvwriter.writerow(head)
      break
    
    count = 1
    for timestamp in joints:
      row = []
      row.append(count)
      row.append(timestamp)
      for data in joints[timestamp]:
        row.append(data['x'])
        row.append(data['y'])
        row.append(data['z'])
      csvwriter.writerow(row)
      count += 1

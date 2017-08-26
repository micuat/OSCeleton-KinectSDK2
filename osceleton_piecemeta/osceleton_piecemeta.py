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

newfilename = 'pm-' + filename
with open(newfilename, 'w', newline='') as csvfile:
  csvfile.write('''PathFileType	4	(X/Y/Z)	%s
DataRate	CameraRate	NumFrames	NumMarkers	Units	OrigDataRate	OrigDataStartFrame	OrigNumFrames
30.00	30.00	      %d	24	mm	30.00	1	      %d
Frame#	Time	Head			SpineShoulder			SpineMid			SpineBase			CollarRight			ShoulderRight			ElbowRight			WristRight			HandRight			FingerRight			CollarLeft			ShoulderLeft			ElbowLeft			WristLeft			HandLeft			FingerLeft			HipRight			KneeRight			AnkleRight			FootRight			HipLeft			KneeLeft			AnkleLeft			FootLeft
		X1	Y1	Z1	X2	Y2	Z2	X3	Y3	Z3	X4	Y4	Z4	X5	Y5	Z5	X6	Y6	Z6	X7	Y7	Z7	X8	Y8	Z8	X9	Y9	Z9	X10	Y10	Z10	X11	Y11	Z11	X12	Y12	Z12	X13	Y13	Z13	X14	Y14	Z14	X15	Y15	Z15	X16	Y16	Z16	X17	Y17	Z17	X18	Y18	Z18	X19	Y19	Z19	X20	Y20	Z20	X21	Y21	Z21	X22	Y22	Z22	X23	Y23	Z23	X24	Y24	Z24\n'''
    % (newfilename, len(joints), len(joints)))
  csvwriter = csv.writer(csvfile, delimiter='\t',
                          quotechar='|', quoting=csv.QUOTE_MINIMAL)
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

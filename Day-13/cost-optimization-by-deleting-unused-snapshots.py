'''
1. List the snapshots in current us-east-1 region
2. If snapshot is not associated with any volume or if associated volume doesn't exist, delete it
3. If snapshot is associated with a volume, then delete the snapshot only if the volume is not attached to any instance
4. This code should trigger every weekend on sunday
'''

import boto3

#def lambda_handler(event, context):

ec2_client = boto3.client('ec2')

# Fetch all snapshots owned by the account
snapshots_dict = ec2_client.describe_snapshots(OwnerIds=['self'])
snapshots_list = snapshots_dict['Snapshots']

# Fetch all volumes in the region
volumes_dict = ec2_client.describe_volumes()
volumes_list = volumes_dict['Volumes']
#print(volumes_list)
#print('--------------------------------------\n')

# Create a set of existing volume IDs
existing_volume_ids = {volume['VolumeId']: volume for volume in volumes_list}
#print(existing_volume_ids)
#print('--------------------------------------\n')

'''
existing_volume_ids = {}        # creating an empty dictionary
for volume in volumes_list:
    existing_volume_ids[volume['VolumeId']] = volume
print(existing_volume_ids)
print('--------------------------------------\n')
'''

for snapshot in snapshots_list:
    snap_id = snapshot["SnapshotId"]
    vol_id = snapshot.get("VolumeId")  # Use get() to avoid KeyError if missing
    #print(vol_id)

    if vol_id is None or vol_id not in existing_volume_ids:
        #ec2_client.delete_snapshot(SnapshotId=snap_id)
        print(f"Snapshot {snap_id} should be 'DELETED' as it's not associated with any existing volume")
    else:
        volume = existing_volume_ids[vol_id]
        #print(volume)
        if volume['State'] == 'in-use':
            #pass
            print(f"Keep the snapshot {snap_id} as the volume {vol_id} is attached to an instance")
        else:
            #ec2_client.delete_snapshot(SnapshotId=snap_id)
            print(f"Volume {vol_id} is not attached to any instance. Hence 'DELETE' the snapshot {snap_id}")

#if "abc" in {'gh': {1,2,3}, 1:'abc', 'abch': 'avb'}:
#    print("exists..")

'''
import boto3

ec2_client = boto3.client('ec2')

snapshots_dict = ec2_client.describe_snapshots(OwnerIds=['self'])
#snapshots_dict = ec2_client.describe_snapshots()
#print("---------------- response_dict -----------------")
#print(snapshots_dict)
   
snapshots_list = snapshots_dict['Snapshots']
print("---------------- snapshots_list -----------------")
print(snapshots_list)

#volumes_dict = ec2_client.describe_volumes(VolumeIds=[])
volumes_dict = ec2_client.describe_volumes()
#print("---------------- volumes_dict -----------------")
#print(volumes_dict)

volumes_list = volumes_dict['Volumes']
print("---------------- volumes_list -----------------")
print(volumes_list)
print("========================================================================")

lt_snap = []
lt_vol = []
for i in range(0, len(snapshots_list)):
    snap_id = snapshots_list[i]["SnapshotId"]
    #print("snap_id = ", snap_id)        
    lt_snap.append(snap_id)

    vol_id = snapshots_list[i]["VolumeId"]
    #print("vol_id = ", vol_id)
    lt_vol.append(vol_id)
        
snap_set = set(lt_snap)
vol_set = set(lt_vol)
print(snap_set)
print(vol_set)

   
for i in range(0, len(volumes_list)):
    for vol in vol_set:
        if vol == volumes_list[i]['VolumeId']: 
            print(volumes_list[i]['VolumeId'])
            print(volumes_list[i]['State'])
            if volumes_list[i]['State'] == 'in-use':       
                print("Keep the snapshot ", snap_id) 
                break
            else:
                print("Volume {} is not attached to any instance. Hence 'DELETE' the snapshot {}".format(vol_id, snap_id))
                break
        else:
            print("Snapshot {} should be 'DELETED' as not associated with any existing volume".format(snap_id))
'''
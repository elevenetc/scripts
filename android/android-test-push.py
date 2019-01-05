# https://github.com/geeknam/python-gcm
import sys

from gcm import GCM

if __name__ == '__main__':
    gcm_token = sys.argv[1]
    device_id = sys.argv[2]

    gcm = GCM(gcm_token)
    data = {'message': 'hello'}
    reg_ids = [device_id]

    gcm.plaintext_request(registration_id=reg_ids, data=data)

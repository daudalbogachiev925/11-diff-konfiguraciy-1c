def compare(old, new):
    old_ids = {o['uuid']: o for o in old}
    new_ids = {o['uuid']: o for o in new}
    added   = [new_ids[k] for k in new_ids.keys() - old_ids.keys()]
    removed = [old_ids[k] for k in old_ids.keys() - new_ids.keys()]
    changed = [new_ids[k] for k in old_ids.keys() & new_ids.keys()
               if old_ids[k]['hash'] != new_ids[k]['hash']]
    return {'added': added, 'removed': removed, 'changed': changed}

import logging

def by_keys(ll_strings):
  logging.debug("nodups!bykeys: received %d strings" % len(ll_strings))
  if ll_strings:
    m = {}
    for s in ll_strings:
      try:
        key, val = s.split(":")
        m[key] = val
      except:
        logging.error("nodups!bykeys: unexpected error encountered, skipping line: %s" % s)
    if m:
      nodups = ["%s: %s" % (k, v) for k, v in m.items()]
      logging.debug("nodups!bykeys: duplicated keys removed to %d strings" % len(nodups))
      return nodups


def by_strings(ll_strings):
  logging.debug("nodups!by_strings: received %d strings" % len(ll_strings))
  if ll_strings:
    nodups = list(set(ll_strings))
    logging.debug("nodups!by_strings: duplicated keys removed to %d strings" % len(nodups))
    return nodups
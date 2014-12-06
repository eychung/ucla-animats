import pickle

class Constants:
  NUM_STATES = 432 # 4*3*2*3*3*2
  NUM_ACTIONS = 5

  # Beaver
  BEAVER_STATE_INDEX_BEAVER_ENERGY = 0
  BEAVER_STATE_INDEX_MARSH_HEALTH = 1
  BEAVER_STATE_INDEX_LUMBER = 2
  BEAVER_STATE_INDEX_TREE = 3
  BEAVER_STATE_INDEX_MARSH = 4
  BEAVER_STATE_INDEX_WOLF = 5

  BEAVER_ACTION_MOVE_TREE = 0
  BEAVER_ACTION_MOVE_MARSH = 1
  BEAVER_ACTION_EAT = 2
  BEAVER_ACTION_PICK_UP_LUMBER = 3
  BEAVER_ACTION_DROP_LUMBER = 4

  BEAVER_STATE_BEAVER_ENERGY_ZERO = "beaver energy zero"
  BEAVER_STATE_BEAVER_ENERGY_LOW = "beaver energy low"
  BEAVER_STATE_BEAVER_ENERGY_MED = "beaver energy med"
  BEAVER_STATE_BEAVER_ENERGY_HIGH = "beaver energy high"
  BEAVER_STATE_MARSH_HEALTH_LOW = "marsh energy low"
  BEAVER_STATE_MARSH_HEALTH_MED = "marsh energy med"
  BEAVER_STATE_MARSH_HEALTH_HIGH = "marsh energy high"
  BEAVER_STATE_HAS_LUMBER = "has lumber"
  BEAVER_STATE_NO_LUMBER = "no lumber"
  BEAVER_STATE_SEE_TREE = "see tree"
  BEAVER_STATE_AT_TREE = "at tree"
  BEAVER_STATE_NONE_TREE = "none tree"
  BEAVER_STATE_SEE_MARSH = "see marsh"
  BEAVER_STATE_AT_MARSH = "at marsh"
  BEAVER_STATE_NONE_MARSH = "none marsh"
  BEAVER_STATE_SEE_WOLF = "see wolf"
  BEAVER_STATE_NONE_WOLF = "none wolf"

  REWARDS = pickle.load(open('rewards.p', 'rb'))
  STATE_TO_INDEX = pickle.load(open('state_to_index.p', 'rb'))
  INDEX_TO_STATE = pickle.load(open('index_to_state.p', 'rb'))

from dataclasses import dataclass

@dataclass
class DataFields:
    # Max/Min/Average
    # length of data messages
    max_len: int
    min_len: int
    avg_len: int
    # Number of data messages
    num_msgs: int
    # Max/Min/Average time 
    # difference between 
    # data messages
    max_delta: float
    min_delta: float
    avg_delta: float
    # Number of DIO/DIS/DAO 
    # messages
    num_dio: int
    num_dis: int
    num_dao: int
    # Max/Min/Average 
    # time difference between
    # DIO/DIS/DAO messages
    max_dio_delta: float
    min_dio_delta: float
    avg_dio_delta: float
    max_dis_delta: float
    min_dis_delta: float
    avg_dis_delta: float
    max_dao_delta: float
    min_dao_delta: float
    avg_dao_delta: float
    # Attack type
    attack_type: str
    # Number of dropped packets due to collision
    # /neighbor allocation/queueing/packeting
    num_collision_drops: int = 0
    num_neigh_alloc_drops: int = 0
    num_queue_drops: int = 0
    num_packetn_drops: int = 0
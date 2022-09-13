class Singleton(object):
    # __new__, 이 __init__ 보다 먼저 실행됨
    def __new__(cls, *args, **kwargs): 
        if not hasattr(cls, "_instance"):           # _instance 속성 : Singleton 객체
            print("__new__ is called")
            cls._instance = super().__new__(cls)    # 객체 생성 및 _instacne key로 바인딩
        return cls._instance                        # _instance return

    def __init__(self, **kwargs):
        cls = type(self)
        if not hasattr(cls, "_init"):               # _init 속성 : Singleton 객체 존재 여부 
            print("__init__ is called")
            self.db_settings = kwargs
            cls._init = True


if __name__ == "__main__":
    # 최초 DB Setting (+ Connection)
    db = Singleton(db_name='mysql',db_port=3306)

    # DB가 연결된 Object Singleton 객체로 소환
    db_object1 = Singleton()
    db_object2 = Singleton()

    print(db)
    print(db_object1)
    print(db_object2)
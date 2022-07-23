## class

# # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데 일반모드 / 시즈모드가 있음
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]". \
#         format(name, location, damage))
    
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

################################################################################
# # 이런식으로는 수십개, 수백개의 유닛을 생성하기 어려움!
# # class를 만들어보자

# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, damage): ## __init__ : 생성자
#         self.name = name # 멤버변수 : class 내에 정의된 변수(self.name, self.hp...)
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)
# # marine1, marine2, tank는 Unit의 인스턴스
# # 인스턴스 생성 시 __init__ 생성자가 호출된다.

# # 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True # 기존 멤버변수는 아님, 추가할 수 있음
# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

################################################################################
## 메소드
## class 내 메소드의 첫번째 파람은 무조건 self
# # 공격 유닛
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".\
#             format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 파이어뱃 : 공격 유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# # 공격을 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

################################################################################
## 상속
# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

# # 공격 유닛
# class AttackUnit(Unit): # AttackUnit은 Unit을 상속받아 만들어짐
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".\
#             format(self.name, location, self.damage))
    
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# # 공격을 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

################################################################################
## 다중 상속 : 부모가 둘 이상
# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

# # 공격 유닛
# class AttackUnit(Unit): # AttackUnit은 Unit을 상속받아 만들어짐
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".\
#             format(self.name, location, self.damage))
    
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
        
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".\
#             format(name, location, self.flying_speed))

# # 공중 공격 유닛 클래스
# # AttackUnit, Flyable 두 개의 클래스 상속 받음
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage) # 초기화
#         Flyable.__init__(self, flying_speed) # 초기화
    
# # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

################################################################################
## 메소드 오버라이딩
# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))

# # 공격 유닛
# class AttackUnit(Unit): # AttackUnit은 Unit을 상속받아 만들어짐
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".\
#             format(self.name, location, self.damage))
    
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
        
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".\
#             format(name, location, self.flying_speed))

# # 공중 공격 유닛 클래스
# # AttackUnit, Flyable 두 개의 클래스 상속 받음
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 초기화, 지상speed=0
#         Flyable.__init__(self, flying_speed) # 초기화

#     def move(self, location): # 메소드 오버라이딩
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# # 벌쳐 : 지상 유닛, 기동성 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
# battlcruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# #battlcruiser.fly(battlcruiser.name, "9시")
# # 메소드 오버라이딩을 통해 똑같은 move 함수를 사용하고자 함
# battlcruiser.move("9시")

################################################################################
## pass

# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass # 아무것도 하지 않고 넘어감

# # 서플라이 디폿 : 건물, 1개 건물당 8 유닛 생성
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()

################################################################################
## super

# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))

# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0) # super를 통한 init 시 self 전달하지 않는다
#         self.location = location

## 새로운 파일로 열어서 실습
# class Unit:
#     def __init__(self):
#         print("Unit 생성자")

# class Flyable:
#     def __init__(self):
#         print("Flyable 생성자")

# class FlyableUnit(Unit, Flyable): # 다중상속
#     def __init__(self):
#         super().__init__()
#         # Unit.__init__(self)
#         # Flyable.__init__(self) # 이처럼 다중상속 시에는 각 부모클래스별로 init 해주어야함

# # 드랍쉽
# dropship = FlyableUnit() # 다중상속시 Unit의 초기화는 탔는데 FlyableUnit 초기화는 타지 않음


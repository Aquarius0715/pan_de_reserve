from .SQLiteManager import *
class Allergy:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Allergy(id={self.id}, name={self.name})"


class BakeryItem:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"BakeryItem(id={self.id}, name={self.name}, price={self.price})"


class BakeryItemAllergy:
    def __init__(self, id, bakery_item_id, allergy_id):
        self.id = id
        self.bakery_item_id = bakery_item_id
        self.allergy_id = allergy_id

    def __repr__(self):
        return f"BakeryItemAllergy(id={self.id}, bakery_item_id={self.bakery_item_id}, allergy_id={self.allergy_id})"


class Reservation:
    def __init__(self, id, receive_time, customer_name, customer_phone_number, is_received):
        self.id = id
        self.receive_time = receive_time
        self.customer_name = customer_name
        self.customer_phone_number = customer_phone_number
        self.is_received = is_received
        self.details = []  # ReservationDetailのリストとして保持

    def __repr__(self):
        return (f"Reservation(id={self.id}, receive_time={self.receive_time}, "
                f"customer_name={self.customer_name}, is_received={self.is_received}, "
                f"details={self.details})")

class ReservationDetail:
    def __init__(self, id, reservation_id, bakery_item, quantity):
        """
        :param id: 予約詳細の ID
        :param reservation_id: 紐づく予約の ID
        :param bakery_item: BakeryItem オブジェクト
        :param quantity: 注文数量
        """
        self.id = id
        self.reservation_id = reservation_id
        self.bakery_item = bakery_item  # BakeryItem オブジェクト
        self.quantity = quantity

    def __repr__(self):
        return (
            f"ReservationDetail(id={self.id}, reservation_id={self.reservation_id}, "
            f"bakery_item={self.bakery_item}, quantity={self.quantity})"
        )


class ReservationService:
    def __init__(self, db_manager: SQLiteManager):
        """
        ReservationServiceは予約関連のデータを操作するクラスです。
        :param db_manager: SQLiteManagerのインスタンス
        """
        self.db_manager = db_manager


    def get_reservations(self):
        reservations_query = """
            SELECT id, receive_time, customer_name, customer_phone_number, is_received
            FROM pan_de_reserve_reservation
        """
        reservation_results = self.db_manager.query(reservations_query)

        # 各予約に関連する詳細情報を取得
        reservations = []
        for res in reservation_results:
            reservation = Reservation(
                id=res[0],
                receive_time=res[1],
                customer_name=res[2],
                customer_phone_number=res[3],
                is_received=res[4],
            )

            # 各予約の詳細情報を取得
            details_query = """
                SELECT rd.id, rd.bakery_item_id, rd.quantity, bi.name, bi.price
                FROM pan_de_reserve_reservationdetail rd
                JOIN pan_de_reserve_bakeryitem bi ON rd.bakery_item_id = bi.id
                WHERE rd.reservation_id = ?
            """
            detail_results = self.db_manager.query(details_query, (reservation.id,))
            for detail in detail_results:
                bakery_item = BakeryItem(
                    id=detail[1],  # bakery_item_id
                    name=detail[3],  # name
                    price=detail[4],  # price
                )
                reservation_detail = ReservationDetail(
                    id=detail[0],
                    reservation_id=reservation.id,
                    bakery_item=bakery_item,
                    quantity=detail[2],
                )
                reservation.details.append(reservation_detail)

            reservations.append(reservation)

        return reservations
    def get_reservation_details(self) -> List[ReservationDetail]:
        """
        予約の詳細をすべて取得します。
        :return: ReservationDetailクラスのリスト
        """
        sql = """
        SELECT id, reservation_id, bakery_item_id, quantity
        FROM pan_de_reserve_reservationdetail
        ORDER BY reservation_id ASC;
        """
        rows = self.db_manager.query(sql)
        return [ReservationDetail(*row) for row in rows]

    def get_reservation_details_by_reservation_id(self, reservation_id: str) -> List[ReservationDetail]:
        """
        指定された予約IDに対応する予約詳細を取得します。
        :param reservation_id: 予約ID
        :return: ReservationDetailクラスのリスト
        """
        sql = """
        SELECT id, reservation_id, bakery_item_id, quantity
        FROM pan_de_reserve_reservationdetail
        WHERE reservation_id = ?
        ORDER BY bakery_item_id ASC;
        """
        rows = self.db_manager.query(sql, (reservation_id,))
        return [ReservationDetail(*row) for row in rows]
    
    def delete_reservation(self, reservation_id: str) -> int:
        """
        予約IDを指定して予約を削除します。
        :param reservation_id: 削除する予約のID
        :return: 削除された行数
        """
        sql = "DELETE FROM pan_de_reserve_reservation WHERE id = ?"
        return self.db_manager.execute(sql, (reservation_id,))


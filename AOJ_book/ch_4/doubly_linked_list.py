class Cell:
    def __init__(self, x):
        self.x = x
        self.next = None
        self.prev = None


class Doubly_linked_list:
    def __init__(self):
        self.head = None

    def insert(self, x):
        new = Cell(x)
        # 現時点での先頭のセル
        tmp_head = self.head

        # headにまだ何も入っていない場合、新しくcellを追加する
        if not tmp_head:
            # 先頭のセルでは、next/prevは自分自身を指す
            new.next = new
            new.prev = new
            self.head = new
            return

        while not tmp_head == self.head:
            tmp_head = tmp_head.next
            print("3", tmp_head)

        print("tmp_head", tmp_head.x)
        # 現時点での先頭セルの場所に新セルをセット
        print("prev", tmp_head.prev.x)
        print("next", tmp_head.next.x)
        print('tmp_head.prev.next',tmp_head.prev.next.x)
        tmp_head.prev.next = new

        # 新セルのprebを現時点での先頭セルのprebに
        new.preb = tmp_head.prev
        # 新セルのnextを現時点での先頭セルに
        new.next = tmp_head
        # 現時点での先頭セルのprebを新セルにする
        tmp_head.prev = new
        print("self.head", self.head.x)

    def show(self):
        tmp_head = self.head
        while tmp_head:
            print(tmp_head.x)
            tmp_head = tmp_head.next
            if tmp_head == self.head:
                return


    # def delete(self,x):
    #     tmp = self.head
    #     if not tmp:
    #         sys.exit('empty')
    #         return
    #     if tmp ==tmp.next:
    #         self.head = tmp = None
    #         return
    #     if tmp.x ==


d = Doubly_linked_list()
print("----insert 3----")
d.insert(3)
print('----show----')
d.show()
print("----insert 4----")
d.insert(4)
print('----show----')
d.show()
print("----insert 5----")
d.insert(5)
print('----show----')
d.show()

import chan_le as bai_1
import luy_thua as bai_2
import y_z_tong_z as bai_3
import tri_tuyet_doi as bai_4

while True:
    action = input("Nhap bai muon kiem tra(1, 2, 3, 4) or Stop: ")
    if action == "1":
        print("Bai 1:")
        while True:
            try:
                n = int(input("n = "))
                if n < 0:
                    print("Positive Integer only")
                else:
                    break
            except ValueError:
                print("Positive Integer only")
        print(bai_1.chan_le(n))
        print()

    elif action == "2":
        print("Bai 2:")
        print(bai_2.luy_thua())
        print()

    elif action == "3":
        print("Bai 3:")
        mang_b_3 = []
        while True:
            try:
                so_phan_tu_b_3 = int(input("So phan tu cua mang x: "))
                if so_phan_tu_b_3 < 0:
                    print("Positive Integer only")
                else:
                    break
            except ValueError:
                print("Positive Integer only")

        for i in range(so_phan_tu_b_3):
            while True:
                try:
                    phan_tu = float(input("Phan tu {0}: ".format(i + 1)))
                    mang_b_3.append(phan_tu)
                    break
                except ValueError:
                    print("Number only")
        print("x: ", mang_b_3)
        print("y: ", bai_3.y_z_tong_z(mang_b_3)[0])
        print("z: ", bai_3.y_z_tong_z(mang_b_3)[1])
        if mang_b_3 == []:
            print("Khong co tong phan tu cua z")
        else:
            print("Tong phan tu cua z: ", round(bai_3.y_z_tong_z(mang_b_3)[2], 2))
        print()
    elif action == "4":
        print("Bai 4")
        mang_b_4 = []
        while True:
            try:
                so_phan_tu_b_4 = int(input("So phan tu cua mang: "))
                if so_phan_tu_b_4 < 0:
                    print("Positive Integer only")
                else:
                    break
            except ValueError:
                print("Positive Integer only")

        for i in range(so_phan_tu_b_4):
            while True:
                try:
                    phan_tu = float(input("Phan tu {0}: ".format(i + 1)))
                    mang_b_4.append(phan_tu)
                    break
                except ValueError:
                    print("Number only")
        print("Mang: ", mang_b_4)
        if mang_b_4 == []:
            print("Khong co tong")
        else:
            print("Tong tri tuyet doi cua mang: ", bai_4.tri_tuyet_doi(mang_b_4))
    elif action == "stop":
        break
    else:
        print("1, 2, 3, 4 or Stop only ...")














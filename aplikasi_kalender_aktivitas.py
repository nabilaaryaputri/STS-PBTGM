class Activity:
    def __init__(self, day, description):
        self.day = day
        self.description = description

    def __str__(self):
        return f"{self.day}: {self.description}"


class Calender:
    def __init__(self):
        self.weekly_schedule = {}  # Memastikan atribut didefinisikan di sini

    def add_activity(self, week, day, description):
        if week in self.weekly_schedule:
            print(f"Minggu {week} sudah memiliki aktivitas.")
        else:
            self.weekly_schedule[week] = Activity(day, description)
            print(f"Berhasil menambahkan aktivitas untuk Minggu {week}.")

    def display_schedule(self):
        if not self.weekly_schedule:
            print("Belum ada jadwal aktivitas.")
            return
        
        print("Jadwal Aktivitas Mingguan:")
        for week, activity in sorted(self.weekly_schedule.items()):
            print(f"Minggu {week}: {activity}")


def main():
    calendar = Calender()

    while True:
        print("\n=== Kalender Aktivitas Mingguan ===")
        print("1. Tambah Aktivitas")
        print("2. Tampilkan Jadwal")
        print("3. Keluar")
        choice = input("Pilih menu: ")

        if choice == "1":
            week = input("Masukkan minggu (contoh: 1): ")
            day = input("Masukkan hari (contoh: Senin): ")
            description = input("Masukkan deskripsi aktivitas: ")
            calendar.add_activity(week, day, description)
        elif choice == "2":
            calendar.display_schedule()
        elif choice == "3":
            print("Keluar dari aplikasi. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")


if __name__ == "__main__":
    main()
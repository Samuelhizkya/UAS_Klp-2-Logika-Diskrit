# -------------------------
# MODUL 4 : GRAF (Interaktif BFS)
# -------------------------
def modul_graf_interaktif():
    try:
        cetak_box("MODUL 4 : GRAF (Rute Rumah Sakit)", [
            "Graf default akan digunakan. Anda bisa memilih titik awal dan tujuan."
        ])
        # Graf sederhana default
        graph = {
            "Lobby": ["Pendaftaran", "UGD"],
            "Pendaftaran": ["Lobby", "Poli Umum", "Poli Gigi"],
            "Poli Umum": ["Pendaftaran", "Farmasi"],
            "Poli Gigi": ["Pendaftaran"],
            "UGD": ["Lobby", "ICU"],
            "ICU": ["UGD"],
            "Farmasi": ["Poli Umum"]
        }

        cetak_box("Nodes di Graf", [f"{k}: {v}" for k, v in graph.items()])

        start = input("Masukkan node awal (contoh: Lobby): ").strip()
        goal = input("Masukkan node tujuan (contoh: Farmasi): ").strip()

        if start not in graph:
            print(f"Node awal '{start}' tidak ditemukan dalam graf.")
            return
        if goal not in graph:
            print(f"Node tujuan '{goal}' tidak ditemukan dalam graf.")
            return

        # BFS mencari rute terpendek (jalan tanpa bobot)
        def bfs(start_node, goal_node):
            queue = deque([[start_node]])
            visited = set()
            while queue:
                path = queue.popleft()
                node = path[-1]
                if node == goal_node:
                    return path
                if node not in visited:
                    visited.add(node)
                    for neighbor in graph.get(node, []):
                        if neighbor not in path:  # hindari loop sederhana
                            new_path = list(path)
                            new_path.append(neighbor)
                            queue.append(new_path)
            return None

        path = bfs(start, goal)
        if path:
            cetak_box("Hasil Pencarian Rute", [f"Rute terpendek: {' -> '.join(path)}", f"Jumlah langkah: {len(path)-1}"])
        else:
            print("Tidak ditemukan rute dari", start, "ke", goal)
    except Exception as e:
        print("Terjadi kesalahan di modul graf:", e)


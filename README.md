1. Penjelasan singkat algoritma greedy yang diimplementasikan
2. Requirement program dan instalasi tertentu bila ada
3. Command atau langkah-langkah dalam meng-compile atau build program 
4. Author (identitas pembuat)

# Diamond2 ©etimo Bot
Tugas Besar 1 IF2211 Strategi Algoritma -  Greedy
Original Diamond2 etimo github : https://github.com/Etimo/diamonds2

<p align="center">
  <img height="360px" src="https://i.ibb.co/Sdphr75/Whats-App-Image-2024-03-09-at-12-39-03-d4a3aeab.jpg" alt="foto"/>
  <br>
  <a><i><sup>Kelompok "Nama Kelompoknya Nanti"</sup></i></a>
</p>

## Anggota 
1. M Athaullah Daffa Kusuma M (13522044)
2. Rafiki Prawira Harianto (13522065)
3. Julian Caleb Simandjuntak (13522099)

## Deskripsi Singkat
Program ini merupakan implementasi bot dengan algoritma Greedy yang telah dibuat. Algoritma greedy yang telah diimplementasikan adalah bot akan mencari diamond terdekat (dan konsiderasi terdekat nomor 2 atau 3 dengan selisih jarak dengan terdekatnya <= 2 jika diamond ini lebih banyak rewardnya daripada yang terdekat), lalu saat bot telah membawa >= 3, bot akan memprioritaskan diri untuk pulang. Saat bot pulang, dan menemukan diamond yang dekat (diamond dengan jarak <= 2) dan masih bisa dimasukkan ke inventory, bot akan mengambil diamond tersebut.

## Cara menjalankan Game Engine 💻
### Requirement
* Node.js (https://nodejs.org/en) 
* Docker desktop (https://www.docker.com/products/docker-desktop/) 
* Yarn
```sh
npm install --global yarn
```
### Instalasi dan konfigurasi awal
1. Download source code (.zip) pada release game engine (https://github.com/haziqam/tubes1-IF2211-game-engine/releases/tag/v1.1.0)
2. Extract zip tersebut, lalu masuk ke folder hasil extractnya dan buka terminal
3. Masuk ke root directory dari project (sesuaikan dengan nama rilis terbaru)
```sh
cd tubes1-IF2110-game-engine-1.1.0
```
4. Install dependencies menggunakan Yarn    
```sh
yarn
```
5. Setup default environment variable dengan menjalankan script berikut
Untuk Windows
```sh
./scripts/copy-env.bat
```
Untuk Linux / (possibly) macOS
```sh
chmod +x ./scripts/copy-env.sh
./scripts/copy-env.sh
```
6. Setup local database (buka aplikasi docker desktop terlebih dahulu, lalu jalankan command berikut di terminal)
```sh
docker compose up -d database
```
Lalu jalankan script berikut. Untuk Windows
```sh
./scripts/setup-db-prisma.bat
```
Untuk Linux / (possibly) macOS
```sh
chmod +x ./scripts/setup-db-prisma.sh
./scripts/setup-db-prisma.sh
``` 

### Build
```sh
npm run build
```

### Run
```sh
npm run start
```
Kunjungi frontend melalui http://localhost:8082/.

## Cara menjalankan Bot 🤖

### Requirement
* Python (https://www.python.org/downloads/) 

### Instalasi dan konfigurasi awal
1. Clone repository ini dan masuk ke src
```sh
git clone https://github.com/Julian-Caleb/Tubes1_Nama-Kelompoknya-Nanti
cd ./src
```
2. Install dependencies
```sh
pip install -r requirements.txt
```

### Menjalankan Bot
1. Untuk run 1 bot
```sh
python main.py --logic LogikanyaNanti --email=your_email@example.com --name=your_name --password=your_password --team etimo
```
2. Untuk run bot banyak
Untuk Windows
```sh
./run-bots.bat
```
Untuk Linux / (possibly) MacOD
```sh
./run-bots.sh
```
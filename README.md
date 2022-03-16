# Airflow Docker

## Pre-requisite

* Install [Docker Community Edition (CE)](https://docs.docker.com/engine/install/) di workstation Anda. Konfigurasi penggunaan memori minimal 4,00 GB agar semua container berjalan dengan baik.
* Install [Docker Compose v1.29.1](https://docs.docker.com/compose/install/) atau yang lebih update di workstation Anda.

Setelah Docker terinstall, Anda harus mengunduh [docker-composer.yaml](https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml) dengan menggunakan `curl` atau `wget`. Sebelumnya, buat folder, misalkan `airflow-docker` pada workstation Anda dan eksekusi command berikut ini di dalam folder tersebut.

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.2/docker-compose.yaml'
```

## Initializing Environment

Sebelum memulai Airflow untuk pertama kalinya, siapkan environment terlebih dahulu, yaitu dengan membuat file, direktori, dan database yang diperlukan. Di dalam folder `airflow-docker` yang telah dibuat, eksekusi command berikut ini.

```bash
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

## Initializing database

Anda perlu menjalankan migrasi database dan membuat akun pengguna pertama pada Airflow dengan menggunakan command berikut ini.

```bash
docker-compose up airflow-init
```
Apabila eksekusi berhasil, akan muncul log seperti berikut ini.

```bash
airflow-init_1       | Upgrades done
airflow-init_1       | Admin user airflow created
airflow-init_1       | 2.2.2
start_airflow-init_1 exited with code 0
```
Secara default, akun yang terbuat memiliki username `airflow` dan password `airflow`.

## Running Airflow

Untuk menjalankan semua service yang ada pada Airflow, kita bisa gunakan command berikut.

```bash
docker-compose up
```

Tunggu sampai semuanya berjalan normal, buka browser Anda dan buka halaman login Airflow dengan alamat `http://localhost:8080/`.

<img src="./airflow-login.png" alt="Airflow Login" width="60%" height="60%"/>

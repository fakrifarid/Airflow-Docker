# DAGs

## DAG: `dag_choose_best_model_ekoteguh`

DAG berikut ini berisi tasks yang sederhana yang berisi:

```python
start >> choose_best_model >> [accurate, inaccurate]
```

`start`, `accurate`, dan `inaccurate` memakai DummyOperator sedangkan `choose_best_model` menggunakan BranchPythonOperator.

Sebagai tambahan untuk tugas berikutnya adalah menghubungkan alert pada `Slack` yang progamnya bisa dilihat pada `alert/slack_alert.py` yang mana akan mengirimkan notifikasi ke Slack pada `#general` task yang berhasil atau success. Selanjutnya, pada DAG `dag_choose_best_model_ekoteguh` baris ke-5 dan ke-11 ditambahkan kode berikut.

```python
# baris ke-5
from alert import slack_alert

# baris ke-11
'on_success_callback': slack_alert.task_send_success_slack_alert
```
Selanjutnya, tinggal aktifkan DAG ini pada Airflow dan buat trigger untuk menjalankan DAG tersebut. Hasilnya adalah sebagai berikut.

![Contoh notifikasi alert Slack](./example-alert.png)
# DAGs

## DAG: `dag_choose_best_model`

DAG berikut ini berisi tasks yang sederhana yang berisi:

```python
start >> branch_task >> [dummy_task_1, dummy_task_2]
```

`start`, `accurate`, dan `inaccurate` memakai DummyOperator sedangkan `choose_best_model` menggunakan BranchPythonOperator.

Sebagai tambahan untuk tugas berikutnya adalah menghubungkan alert pada `Slack` yang progamnya bisa dilihat pada `alert/slack_alert.py` yang mana akan mengirimkan notifikasi ke Slack pada `#general` task yang berhasil atau success. Selanjutnya, pada DAG `dag_choose_best_model` baris ke-2 dan ke-10 ditambahkan kode berikut.

```python
# baris ke-2
from alert import slack_alert

# baris ke-10
'on_success_callback': slack_alert.task_send_success_slack_alert
```
Selanjutnya, tinggal aktifkan DAG ini pada Airflow dan buat trigger untuk menjalankan DAG tersebut. Hasilnya adalah sebagai berikut.

![image](https://user-images.githubusercontent.com/95616496/158543040-c812e15f-97b8-48eb-a910-1ade15a0c421.png)


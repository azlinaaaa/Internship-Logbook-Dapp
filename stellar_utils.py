from stellar_sdk import Server, Keypair, TransactionBuilder, Network
from stellar_sdk.exceptions import NotFoundError
import hashlib
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Sediakan sambungan Horizon Server
server = Server("https://horizon-testnet.stellar.org")
secret_key = os.getenv("STELLAR_SECRET_KEY")


def hash_log(content):
    return hashlib.sha256(content.encode()).hexdigest()


def store_hash_on_stellar(log_hash):
    # 1. Jana Keypair secara automatik daripada Secret Key
    source_keypair = Keypair.from_secret(secret_key)

    # 2. Dapatkan Public Key secara dinamik (Tak perlu ambil dari .env lagi)
    public_key = source_keypair.public_key

    # 3. Semakan keselamatan: Aktifkan akaun guna Friendbot jika belum wujud (Ralat 404)
    try:
        source_account = server.load_account(public_key)
    except NotFoundError:
        print(f"Akaun {public_key} belum aktif di Testnet. Mengaktifkan via Friendbot...")
        friendbot_response = requests.get(f"https://friendbot.stellar.org/?addr={public_key}")
        if friendbot_response.status_code == 200:
            print("Akaun berjaya diaktifkan!")
            source_account = server.load_account(public_key)
        else:
            raise Exception("Gagal mengaktifkan akaun melalui Friendbot Testnet.")

    # 4. Bina Transaksi Stellar
    transaction = (
        TransactionBuilder(
            source_account=source_account,
            network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
            base_fee=100,
        )
        .append_manage_data_op(
            data_name="internlog",
            data_value=log_hash.encode('utf-8')  # WAJIB di-encode ke bytes supaya tak crash
        )
        .set_timeout(30)
        .build()
    )

    # 5. Tandatangan transaksi menggunakan keypair asal
    transaction.sign(source_keypair)

    # 6. Hantar ke rangkaian Stellar
    response = server.submit_transaction(transaction)

    return response
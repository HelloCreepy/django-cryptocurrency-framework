# Copyright 2019-2020 Alexander Polishchuk
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pytest

from django_obm import models


class TestNodeManager:
    @staticmethod
    @pytest.mark.django_db
    @pytest.mark.usefixtures("bitcoin_core_node", "geth_node")
    def test_collect_transactions():
        txs = models.Node.objects.collect_transactions()
        for tx in txs:
            tx_from_db = models.Transaction.objects.filter(txid=tx.txid).first()
            assert tx_from_db
            assert tx_from_db.pk is not None

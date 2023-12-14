# coding=utf-8
# Copyright 2022 Google SwitchTransformers Authors and HuggingFace Inc. team.
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


from transformers.models.sigma_moe import (
    SigmaMoEConfiguration,
    SigmaMoEFeedForwardLayer,
    SigmaMoEDecoderLayer,
    SigmaMoEModel,
    SigmaMoEForCausalLM,
    SigmaMoEForSequenceClassification,
    SigmaMoEForTokenClassification
)

if __name__ == "__main__":
    import torch

    bs = 5
    seq_len = 128
    d_model = 256

    config = SigmaMoEConfiguration()
    # ff = SigmaMoEFeedForwardLayer(config, is_sparse=True)
    # x = torch.randn((bs, seq_len, d_model), device=torch.device("cpu"))
    # ff(x)

    # decoder_layer = SigmaMoEDecoderLayer(config, is_sparse=True, layer_idx=0)
    # tgt_len = 128
    # src_len = 128
    # hidden_states = torch.randn((bs, seq_len, d_model), device=torch.device("cpu"))
    # mask = torch.tril(torch.ones((bs, 1, tgt_len, src_len), device=torch.device("cpu")))
    # decoder_layer(hidden_states, mask)

    # model = SigmaMoEModel(config)
    # xx = model(input_ids=torch.randint(0, 51200, (bs, seq_len)), return_dict=True)

    # model = SigmaMoEForCausalLM(config)
    # input_ids = torch.randint(0, 51200, (bs, seq_len))
    # xx = model(input_ids=input_ids, return_dict=True, labels=input_ids)

    config.num_labels = 2
    model = SigmaMoEForSequenceClassification(config)
    input_ids = torch.randint(0, 51200, (bs, seq_len))
    labels = torch.randint(0, 2, (bs,))
    xx = model(input_ids=input_ids, return_dict=True, labels=labels)
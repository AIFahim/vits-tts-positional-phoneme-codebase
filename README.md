# vits-tts-positional-phoneme-codebase

### Puntuations Mapping:
```sh
{
    "।": "p1",
    "?": "p2",
    "!": "p3",
    ",": "p4",
    ";": "p5",
    ":—": "p6",
    ":": "p7",
    "—": "p8",
    "“": "p9",
    "”": "p10",
    "‘": "p11",
    "’": "p12",
    "'": "p13",
    "\"": "p14"
}
```
### Positional Phoneme Characters List:
```sh
['a', 'a_1', 'a_2', 'ã', 'ã_1', 'ã_2', 'b', 'b_1', 'b_2', 'bʰ', 'bʰ_1', 'bʰ_2', 'bʱ', 'bʱ_1', 'bʱ_2', 'c', 'c_1', 'c_2', 'cʰ', 'cʰ_1', 'cʰ_2', 'd', 'd_1', 'd_2', 'dʰ', 'dʰ_1', 'dʰ_2', 'dʱ', 'dʱ_1', 'dʱ_2', 'd̪', 'd̪_1', 'd̪_2', 'd̪ʰ', 'd̪ʰ_1', 'd̪ʰ_2', 'd̪ʱ', 'd̪ʱ_1', 'd̪ʱ_2', 'e', 'e_1', 'e_2', 'ẽ', 'ẽ_1', 'ẽ_2', 'e̯', 'e̯_1', 'e̯_2', 'g', 'g_1', 'g_2', 'gʰ', 'gʰ_1', 'gʰ_2', 'gʱ', 'gʱ_1', 'gʱ_2', 'h', 'h_1', 'h_2', 'i', 'i_1', 'i_2', 'ĩ', 'ĩ_1', 'ĩ_2', 'i̯', 'i̯_1', 'i̯_2', 'k', 'k_1', 'k_2', 'kʰ', 'kʰ_1', 'kʰ_2', 'l', 'l_1', 'l_2', 'm', 'm_1', 'm_2', 'n', 'n_1', 'n_2', 'o', 'o_1', 'o_2', 'õ', 'õ_1', 'õ_2', 'o̯', 'o̯_1', 'o̯_2', 'p', 'p_1', 'p_2', 'pʰ', 'pʰ_1', 'pʰ_2', 'r', 'r_1', 'r_2', 's', 's_1', 's_2', 't', 't_1', 't_2', 'tʰ', 'tʰ_1', 'tʰ_2', 't̪', 't̪_1', 't̪_2', 't̪ʰ', 't̪ʰ_1', 't̪ʰ_2', 'u', 'u_1', 'u_2', 'ũ', 'ũ_1', 'ũ_2', 'u̯', 'u̯_1', 'u̯_2', 'æ', 'æ_1', 'æ_2', 'æ̃', 'æ̃_1', 'æ̃_2', 'ŋ', 'ŋ_1', 'ŋ_2', 'ɔ', 'ɔ_1', 'ɔ_2', 'ɔ̃', 'ɔ̃_1', 'ɔ̃_2', 'ɟ', 'ɟ_1', 'ɟ_2', 'ɟʰ', 'ɟʰ_1', 'ɟʰ_2', 'ɽ', 'ɽ_1', 'ɽ_2', 'ɽʰ', 'ɽʰ_1', 'ɽʰ_2', 'ɽʱ', 'ɽʱ_1', 'ɽʱ_2', 'ʃ', 'ʃ_1', 'ʃ_2', 'ʲ', 'ʲ_1', 'ʲ_2', 'ʷ', 'ʷ_1', 'ʷ_2', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14']
```

### Important Packages accordings to the version need to install as follow:
[At first Need to install requirment.txt then need to reinstall below packages with versions]
torch version 1.13.1
Python version - 3.9.0 
Torchaudio version: 0.13.1
### Changes Made inside Codebase for Positional Phonemes:
- [train_fs2.py](https://github.com/AIFahim/testgit/blob/master/train_fs2.py) : Positional phoneme characters list added, And tokens -> ('<PAD>', '<EOS>','<BOS>','<BLNK>') added.
- [characters.py](https://github.com/AIFahim/testgit/blob/master/TTS/tts/utils/text/characters.py): Added positional phoneme characters characters list to the _characters & _vocab variables. Changes made in _create_vocab() - method.

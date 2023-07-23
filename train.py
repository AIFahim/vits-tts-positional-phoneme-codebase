import os
from TTS.tts.configs.shared_configs import BaseDatasetConfig,BaseAudioConfig,CharactersConfig
from TTS.tts.configs.glow_tts_config import GlowTTSConfig

from TTS.tts.configs.vits_config import VitsConfig
from TTS.tts.models.vits import Vits, VitsAudioConfig


from TTS.utils.audio import AudioProcessor
from TTS.tts.utils.text.tokenizer import TTSTokenizer
from TTS.tts.models.glow_tts import GlowTTS
from TTS.tts.datasets import load_tts_samples
from trainer import Trainer, TrainerArgs

def main():
    os.environ["CUDA_LAUNCH_BLOCKING"]=  '1'
    # BaseDatasetConfig: defines name, formatter and path of the dataset.
    output_path = "checkpoints_bn_female"

    dataset_config = BaseDatasetConfig(
        formatter="ljspeech", meta_file_train="/UPDS/TTS/train_jubayer/metadata_grapheme_phoneme.txt", path="/UPDS/TTS/train_jubayer/" # os.path.join(output_path, "LJSpeech-1.1/"
    )


    my_valid_lis= ['a', 'a_1', 'a_2', 'ã', 'ã_1', 'ã_2', 'b', 'b_1', 'b_2', 'bʰ', 'bʰ_1', 'bʰ_2', 'bʱ', 'bʱ_1', 'bʱ_2', 'c', 'c_1', 'c_2', 'cʰ', 'cʰ_1', 'cʰ_2', 'd', 'd_1', 'd_2', 'dʰ', 'dʰ_1', 'dʰ_2', 'dʱ', 'dʱ_1', 'dʱ_2', 'd̪', 'd̪_1', 'd̪_2', 'd̪ʰ', 'd̪ʰ_1', 'd̪ʰ_2', 'd̪ʱ', 'd̪ʱ_1', 'd̪ʱ_2', 'e', 'e_1', 'e_2', 'ẽ', 'ẽ_1', 'ẽ_2', 'e̯', 'e̯_1', 'e̯_2', 'g', 'g_1', 'g_2', 'gʰ', 'gʰ_1', 'gʰ_2', 'gʱ', 'gʱ_1', 'gʱ_2', 'h', 'h_1', 'h_2', 'i', 'i_1', 'i_2', 'ĩ', 'ĩ_1', 'ĩ_2', 'i̯', 'i̯_1', 'i̯_2', 'k', 'k_1', 'k_2', 'kʰ', 'kʰ_1', 'kʰ_2', 'l', 'l_1', 'l_2', 'm', 'm_1', 'm_2', 'n', 'n_1', 'n_2', 'o', 'o_1', 'o_2', 'õ', 'õ_1', 'õ_2', 'o̯', 'o̯_1', 'o̯_2', 'p', 'p_1', 'p_2', 'pʰ', 'pʰ_1', 'pʰ_2', 'r', 'r_1', 'r_2', 's', 's_1', 's_2', 't', 't_1', 't_2', 'tʰ', 'tʰ_1', 'tʰ_2', 't̪', 't̪_1', 't̪_2', 't̪ʰ', 't̪ʰ_1', 't̪ʰ_2', 'u', 'u_1', 'u_2', 'ũ', 'ũ_1', 'ũ_2', 'u̯', 'u̯_1', 'u̯_2', 'æ', 'æ_1', 'æ_2', 'æ̃', 'æ̃_1', 'æ̃_2', 'ŋ', 'ŋ_1', 'ŋ_2', 'ɔ', 'ɔ_1', 'ɔ_2', 'ɔ̃', 'ɔ̃_1', 'ɔ̃_2', 'ɟ', 'ɟ_1', 'ɟ_2', 'ɟʰ', 'ɟʰ_1', 'ɟʰ_2', 'ɽ', 'ɽ_1', 'ɽ_2', 'ɽʰ', 'ɽʰ_1', 'ɽʰ_2', 'ɽʱ', 'ɽʱ_1', 'ɽʱ_2', 'ʃ', 'ʃ_1', 'ʃ_2', 'ʲ', 'ʲ_1', 'ʲ_2', 'ʷ', 'ʷ_1', 'ʷ_2', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14']

    characters_config = CharactersConfig(
        pad = '<PAD>',#'<PAD>',
        eos = '<EOS>',#'\n', #'<EOS>', #'।',
        bos = '<BOS>',#'<BOS>',# None,
        blank = '<BLNK>',#'<BLNK>',
        phonemes = None,
        characters = my_valid_lis ,#char_sen,
        punctuations = '' # "-!,|.? ",
    )


    audio_config = VitsAudioConfig(
        sample_rate=48000,
        win_length=1024,
        hop_length=256,
        num_mels=80,
        mel_fmin=0,
        mel_fmax=None,
    )
    

    
    config =  VitsConfig(
        batch_size=64,
        eval_batch_size=128,
        num_loader_workers=16,
        num_eval_loader_workers=16,
        batch_group_size=5,
        run_eval=True,
        test_delay_epochs=-1,
        epochs=5000,
        text_cleaner= "collapse_whitespace", #"collapse_whitespace",
        # compute_input_seq_cache=True,
        use_phonemes=False,
        # phoneme_language="bn",
        phoneme_cache_path=os.path.join(output_path, "phoneme_cache"),
        print_step=25,
        print_eval=False,
        mixed_precision=False,
        output_path=output_path,
        datasets=[dataset_config],
        save_step=1000,
        audio=audio_config,
        characters=characters_config,
        cudnn_benchmark=False,
        test_sentences = [
            "ʃ_1 ɔ n n o b o t̪ i_2 ɔ_1 r t̪ t̪ʰ o_2 cʰ_1 i ʲ a n ɔ b b o i̯_2 ʃ_1 o ŋ kʰ o k_2" #ষণ্নবতি অর্থ ছিয়ানব্বই সংখ্যক।|
        ],
    )


    
    ap = AudioProcessor.init_from_config(config)
    tokenizer, config = TTSTokenizer.init_from_config(config)


    def formatter(root_path, meta_file, **kwargs):  # pylint: disable=unused-argument
        """Normalizes the LJSpeech meta data file to TTS format
        https://keithito.com/LJ-Speech-Dataset/"""
        txt_file = meta_file
        items = []
        speaker_name = "ljspeech"
        with open(txt_file, "r", encoding="utf-8") as ttf:
            for line in ttf:
                cols = line.split("|")
                wav_file = os.path.join(root_path, "wavs", cols[0] + ".wav")
                try:
                    text = cols[2]
                except:
                    print("not found")

                items.append({"text": text, "audio_file": wav_file, "speaker_name": speaker_name, "root_path": root_path})
        return items

    
    train_samples, eval_samples = load_tts_samples(
        dataset_config,
        eval_split=True,
        eval_split_max_size=config.eval_split_max_size,
        eval_split_size=config.eval_split_size,
        formatter=formatter,
    )


    
    model = Vits(config, ap, tokenizer, speaker_manager=None)


    
    trainer = Trainer(
        TrainerArgs(), config, output_path, model=model, train_samples=train_samples, eval_samples=eval_samples
    )

    trainer.fit()

if __name__ == "__main__":
    main()

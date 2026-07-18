@echo off
:: Create the main folder for Audio Preprocessing
mkdir "Audio_Preprocessing"

:: Change to the Audio Preprocessing directory
cd "Audio_Preprocessing"

:: 1. Introduction to Audio Preprocessing
mkdir "01_Introduction_to_Audio_Preprocessing"
mkdir "01_Introduction_to_Audio_Preprocessing\01_ What_is_Audio_Preprocessing"
mkdir "01_Introduction_to_Audio_Preprocessing\02_ Applications_in_Audio_Processing"
mkdir "01_Introduction_to_Audio_Preprocessing\03_ Overview_of_Audio_Tools_and_Libraries"

:: 2. Understanding Audio Data
mkdir "02_Understanding_Audio_Data"
mkdir "02_Understanding_Audio_Data\01_ Digital_Audio_Basics"
mkdir "02_Understanding_Audio_Data\02_ Sampling_and_Bit_Depth"
mkdir "02_Understanding_Audio_Data\03_ Audio_Formats_(WAV_MP3_FLAC)"
mkdir "02_Understanding_Audio_Data\04_ Time_and_Frequency_Domain"

:: 3. Audio Data Loading
mkdir "03_Audio_Data_Loading"
mkdir "03_Audio_Data_Loading\01_ Using_Libraries_(Librosa_PyDub_AudioKit)"
mkdir "03_Audio_Data_Loading\02_ Reading_and_Writing_Audio_Files"
mkdir "03_Audio_Data_Loading\03_ Resampling_and_Converting_Audio"
mkdir "03_Audio_Data_Loading\04_ Visualizing_Audio_Waveforms"

:: 4. Noise Reduction
mkdir "04_Noise_Reduction"
mkdir "04_Noise_Reduction\01_ Introduction_to_Noise_Reduction"
mkdir "04_Noise_Reduction\02_ Spectral_Subtraction_Method"
mkdir "04_Noise_Reduction\03_ Wiener_Filtering"
mkdir "04_Noise_Reduction\04_ Deep_Learning_for_Noise_Cancellation"

:: 5. Audio Normalization
mkdir "05_Audio_Normalization"
mkdir "05_Audio_Normalization\01_ Amplitude_Normalization"
mkdir "05_Audio_Normalization\02_ Peak_Normalization"
mkdir "05_Audio_Normalization\03_ RMS_Normalization"
mkdir "05_Audio_Normalization\04_ LUFS_Normalization"

:: 6. Feature Extraction
mkdir "06_Feature_Extraction"
mkdir "06_Feature_Extraction\01_ MFCC_(Mel-Frequency_Cepstral_Coefficients)"
mkdir "06_Feature_Extraction\02_ Spectrograms_and_Mel-Spectrograms"
mkdir "06_Feature_Extraction\03_ Chroma_Features"
mkdir "06_Feature_Extraction\04_ Zero-Crossing_Rate"
mkdir "06_Feature_Extraction\05_ Spectral_Centroid_and_Rolloff"
mkdir "06_Feature_Extraction\06_ Temporal_Features_(Energy_Silence)"

:: 7. Data Augmentation
mkdir "07_Data_Augmentation"
mkdir "07_Data_Augmentation\01_ Time_Stretching"
mkdir "07_Data_Augmentation\02_ Pitch_Shifting"
mkdir "07_Data_Augmentation\03_ Adding_Background_Noise"
mkdir "07_Data_Augmentation\04_ Random_Cropping"
mkdir "07_Data_Augmentation\05_ Volume_Manipulation"

:: 8. Audio Segmentation
mkdir "08_Audio_Segmentation"
mkdir "08_Audio_Segmentation\01_ Voice_Activity_Detection_(VAD)"
mkdir "08_Audio_Segmentation\02_ Speaker_Diarization"
mkdir "08_Audio_Segmentation\03_ Silence_Removal"
mkdir "08_Audio_Segmentation\04_ Audio_Chunking"

:: 9. Audio Filtering
mkdir "09_Audio_Filtering"
mkdir "09_Audio_Filtering\01_ Low-Pass_and_High-Pass_Filters"
mkdir "09_Audio_Filtering\02_ Band-Pass_and_Band-Stop_Filters"
mkdir "09_Audio_Filtering\03_ Fourier_Transform_and_Filtering"
mkdir "09_Audio_Filtering\04_ FIR_and_IIR_Filters"

:: 10. Advanced Audio Techniques
mkdir "10_Advanced_Audio_Techniques"
mkdir "10_Advanced_Audio_Techniques\01_ Speech_Enhancement"
mkdir "10_Advanced_Audio_Techniques\02_ Source_Separation"
mkdir "10_Advanced_Audio_Techniques\03_ Audio_Synthesis_and_Generation"
mkdir "10_Advanced_Audio_Techniques\04_ Acoustic_Echo_Cancellation"

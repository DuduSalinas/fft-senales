fs = 1000; T = 1.0; N = fs*T; t = (0:N-1)/fs;
x_chirp = [sin(2*pi*50*t(1:N/2)), sin(2*pi*150*t(N/2+1:end))];

nperseg = 128; noverlap = 96;
w = hamming(nperseg);
[~, f, t_stft, S] = spectrogram(x_chirp, w, noverlap, nperseg, fs, 'yaxis');

figure('Position',[100 100 900 500]);
imagesc(t_stft, f, 20*log10(abs(S)+1e-12)); axis xy; colormap magma;
title(sprintf('Espectrograma STFT (Hamming, nperseg=%d, overlap=%d)', nperseg, noverlap));
xlabel('Tiempo [s]'); ylabel('Frecuencia [Hz]'); colorbar; set(gcf,'Color','w');
if ~exist('figures','dir'), mkdir('figures'); end
saveas(gcf, fullfile('figures','stft_espectrograma_matlab.png'));

% Comparación de ventanas en STFT
wtypes = {'hamming','hann','blackman'};
figure('Position',[100 100 900 800]);
for i=1:numel(wtypes)
    w = window(str2func(wtypes{i}), nperseg);
    [~, f, t_stft, S] = spectrogram(x_chirp, w, noverlap, nperseg, fs, 'yaxis');
    subplot(numel(wtypes),1,i);
    imagesc(t_stft, f, 20*log10(abs(S)+1e-12)); axis xy; colormap magma;
    title(['STFT ventana ' wtypes{i}]); xlabel('Tiempo [s]'); ylabel('Frecuencia [Hz]');
end
set(gcf,'Color','w'); saveas(gcf, fullfile('figures','stft_ventanas_matlab.png'));
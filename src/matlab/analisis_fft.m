% Parámetros
fs = 1000; T = 1.0; N = fs*T; t = (0:N-1)/fs;

%% 
% Funciones utilitarias
fft_mag_phase = @(x) deal(fftshift((-fs/2):(fs/N):(fs/2 - fs/N)), ...
    abs(fftshift(fft(x))), angle(fftshift(fft(x))));

function plot_time_freq(t,x,f,mag,phase,title_base,save_prefix)
    figure('Position',[100 100 1000 600]);
    subplot(2,2,1); plot(t,x,'LineWidth',1.5); title([title_base ' - Tiempo']); xlabel('Tiempo [s]'); ylabel('Amplitud'); grid on;
    subplot(2,2,2); plot(f,mag,'LineWidth',1.5); title([title_base ' - Magnitud']); xlabel('Frecuencia [Hz]'); ylabel('|X(f)|'); grid on;
    subplot(2,2,4); plot(f,phase,'LineWidth',1.0); title([title_base ' - Fase']); xlabel('Frecuencia [Hz]'); ylabel('∠X(f) [rad]'); grid on;
    set(gcf,'Color','w'); if ~exist('figures','dir'), mkdir('figures'); end
    saveas(gcf, fullfile('figures',[save_prefix '.png']));
end

% Señales
f0 = 50; A = 1.0; x_sine = A*sin(2*pi*f0*t);
[f_sine, mag_sine, phase_sine] = fft_mag_phase(x_sine); plot_time_freq(t,x_sine,f_sine,mag_sine,phase_sine,'Senoidal 50 Hz','senoidal_50Hz_matlab');

x_step = ones(size(t));
[f_step, mag_step, phase_step] = fft_mag_phase(x_step); plot_time_freq(t,x_step,f_step,mag_step,phase_step,'Escalón truncado','escalon_truncado_matlab');

width = 0.2; x_rect = double((t >= 0.0) & (t < width));
[f_rect, mag_rect, phase_rect] = fft_mag_phase(x_rect); plot_time_freq(t,x_rect,f_rect,mag_rect,phase_rect,'Pulso rectangular (0.2 s)','pulso_rectangular_matlab');

% Propiedades
a=0.7; b=0.3; x_lin = a*x_sine + b*x_rect;
[f_lin, mag_lin, phase_lin] = fft_mag_phase(x_lin); plot_time_freq(t,x_lin,f_lin,mag_lin,phase_lin,'Linealidad: 0.7*seno + 0.3*pulso','linealidad_matlab');

t0 = 0.1; shift_samples = round(t0*fs); x_rect_shift = circshift(x_rect, [0 shift_samples]);
[f_shift, mag_shift, phase_shift] = fft_mag_phase(x_rect_shift); plot_time_freq(t,x_rect_shift,f_shift,mag_shift,phase_shift,'Pulso desplazado 0.1 s','pulso_desplazado_matlab');

f0_2 = 100; x_sine_fast = A*sin(2*pi*f0_2*t);
[f_fast, mag_fast, phase_fast] = fft_mag_phase(x_sine_fast); plot_time_freq(t,x_sine_fast,f_fast,mag_fast,phase_fast,'Senoidal 100 Hz (escalado en tiempo)','senoidal_100Hz_matlab');

% Ventanas y padding
w_names = {'rectwin','hamming','hann','blackman'};
figure('Position',[100 100 900 500]); hold on;
for k=1:numel(w_names)
    w = window(str2func(w_names{k}), N);
    Xw = fftshift(fft(x_sine(:).*w(:)));
    f = fftshift(((0:N-1)/N)*fs - fs/2);
    plot(f, abs(Xw), 'DisplayName', w_names{k});
end
title('Comparación de ventanas (seno 50 Hz)'); xlabel('Frecuencia [Hz]'); ylabel('|X(f)|'); grid on; legend; set(gcf,'Color','w');
saveas(gcf, fullfile('figures','ventanas_comparacion_matlab.png'));

pad_factor = 4;
X_pad = fft(x_sine, N*pad_factor);
f_pad = fftshift(((0:N*pad_factor-1)/(N*pad_factor))*fs - fs/2);
figure('Position',[100 100 900 500]); 
plot(f_sine, mag_sine, 'DisplayName','Sin padding'); hold on;
plot(f_pad, abs(fftshift(X_pad)), 'DisplayName',['Padding x' num2str(pad_factor)]);
title('Magnitud con y sin padding (seno 50 Hz)'); xlabel('Frecuencia [Hz]'); ylabel('|X(f)|'); grid on; legend; set(gcf,'Color','w');
saveas(gcf, fullfile('figures','senoidal_padding_matlab.png'));
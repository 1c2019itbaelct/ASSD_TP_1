#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Mar 30 17:29:20 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import epy_module_0  # embedded python module
import sip
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.fs0 = fs0 = 100000
        self.freq0 = freq0 = 2500
        self.dutycycle0 = dutycycle0 = 0.5
        self.syh_on = syh_on = True
        self.switch_on = switch_on = True
        self.seniales_control_iguales = seniales_control_iguales = 0
        self.samp_rate = samp_rate = 300000
        self.input_signal = input_signal = 0
        self.input_freq = input_freq = freq0
        self.fs = fs = fs0
        self.filtro_recuperador_on = filtro_recuperador_on = True
        self.filtro_antialiasing_on = filtro_antialiasing_on = True
        self.dutycycle = dutycycle = dutycycle0

        ##################################################
        # Blocks
        ##################################################
        self.main_tab = Qt.QTabWidget()
        self.main_tab_widget_0 = Qt.QWidget()
        self.main_tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_0)
        self.main_tab_grid_layout_0 = Qt.QGridLayout()
        self.main_tab_layout_0.addLayout(self.main_tab_grid_layout_0)
        self.main_tab.addTab(self.main_tab_widget_0, '')
        self.top_grid_layout.addWidget(self.main_tab)
        self.gui_tab_configuracion = Qt.QTabWidget()
        self.gui_tab_configuracion_widget_0 = Qt.QWidget()
        self.gui_tab_configuracion_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.gui_tab_configuracion_widget_0)
        self.gui_tab_configuracion_grid_layout_0 = Qt.QGridLayout()
        self.gui_tab_configuracion_layout_0.addLayout(self.gui_tab_configuracion_grid_layout_0)
        self.gui_tab_configuracion.addTab(self.gui_tab_configuracion_widget_0, 'Streamline')
        self.gui_tab_configuracion_widget_1 = Qt.QWidget()
        self.gui_tab_configuracion_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.gui_tab_configuracion_widget_1)
        self.gui_tab_configuracion_grid_layout_1 = Qt.QGridLayout()
        self.gui_tab_configuracion_layout_1.addLayout(self.gui_tab_configuracion_grid_layout_1)
        self.gui_tab_configuracion.addTab(self.gui_tab_configuracion_widget_1, 'Inputs')
        self.main_tab_grid_layout_0.addWidget(self.gui_tab_configuracion, 0, 0, 1, 1)
        for r in range(0, 1):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        _syh_on_check_box = Qt.QCheckBox("Sample and hold on")
        self._syh_on_choices = {True: 1, False: 0}
        self._syh_on_choices_inv = dict((v,k) for k,v in self._syh_on_choices.iteritems())
        self._syh_on_callback = lambda i: Qt.QMetaObject.invokeMethod(_syh_on_check_box, "setChecked", Qt.Q_ARG("bool", self._syh_on_choices_inv[i]))
        self._syh_on_callback(self.syh_on)
        _syh_on_check_box.stateChanged.connect(lambda i: self.set_syh_on(self._syh_on_choices[bool(i)]))
        self.gui_tab_configuracion_grid_layout_0.addWidget(_syh_on_check_box, 0, 0, 1, 1)
        for r in range(0, 1):
            self.gui_tab_configuracion_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.gui_tab_configuracion_grid_layout_0.setColumnStretch(c, 1)
        _switch_on_check_box = Qt.QCheckBox("Llave analogica on")
        self._switch_on_choices = {True: 1, False: 0}
        self._switch_on_choices_inv = dict((v,k) for k,v in self._switch_on_choices.iteritems())
        self._switch_on_callback = lambda i: Qt.QMetaObject.invokeMethod(_switch_on_check_box, "setChecked", Qt.Q_ARG("bool", self._switch_on_choices_inv[i]))
        self._switch_on_callback(self.switch_on)
        _switch_on_check_box.stateChanged.connect(lambda i: self.set_switch_on(self._switch_on_choices[bool(i)]))
        self.gui_tab_configuracion_grid_layout_0.addWidget(_switch_on_check_box, 0, 1, 1, 1)
        for r in range(0, 1):
            self.gui_tab_configuracion_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.gui_tab_configuracion_grid_layout_0.setColumnStretch(c, 1)
        self._seniales_control_iguales_options = (0, 1, )
        self._seniales_control_iguales_labels = ('Iguales', 'Invertidas', )
        self._seniales_control_iguales_tool_bar = Qt.QToolBar(self)
        self._seniales_control_iguales_tool_bar.addWidget(Qt.QLabel('Relacion seniales control'+": "))
        self._seniales_control_iguales_combo_box = Qt.QComboBox()
        self._seniales_control_iguales_tool_bar.addWidget(self._seniales_control_iguales_combo_box)
        for label in self._seniales_control_iguales_labels: self._seniales_control_iguales_combo_box.addItem(label)
        self._seniales_control_iguales_callback = lambda i: Qt.QMetaObject.invokeMethod(self._seniales_control_iguales_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._seniales_control_iguales_options.index(i)))
        self._seniales_control_iguales_callback(self.seniales_control_iguales)
        self._seniales_control_iguales_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_seniales_control_iguales(self._seniales_control_iguales_options[i]))
        self.gui_tab_configuracion_grid_layout_1.addWidget(self._seniales_control_iguales_tool_bar, 0, 1, 1, 1)
        for r in range(0, 1):
            self.gui_tab_configuracion_grid_layout_1.setRowStretch(r, 1)
        for c in range(1, 2):
            self.gui_tab_configuracion_grid_layout_1.setColumnStretch(c, 1)
        self._input_signal_options = (0, 1, 2, )
        self._input_signal_labels = ('Seno', 'Diente de sierra', 'Seno 3/2', )
        self._input_signal_tool_bar = Qt.QToolBar(self)
        self._input_signal_tool_bar.addWidget(Qt.QLabel("input_signal"+": "))
        self._input_signal_combo_box = Qt.QComboBox()
        self._input_signal_tool_bar.addWidget(self._input_signal_combo_box)
        for label in self._input_signal_labels: self._input_signal_combo_box.addItem(label)
        self._input_signal_callback = lambda i: Qt.QMetaObject.invokeMethod(self._input_signal_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._input_signal_options.index(i)))
        self._input_signal_callback(self.input_signal)
        self._input_signal_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_input_signal(self._input_signal_options[i]))
        self.gui_tab_configuracion_grid_layout_1.addWidget(self._input_signal_tool_bar, 0, 0, 1, 1)
        for r in range(0, 1):
            self.gui_tab_configuracion_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.gui_tab_configuracion_grid_layout_1.setColumnStretch(c, 1)
        self._input_freq_range = Range(freq0/10, freq0*10, freq0/100, freq0, 200)
        self._input_freq_win = RangeWidget(self._input_freq_range, self.set_input_freq, 'Frecuencia senial de entrada', "counter_slider", float)
        self.gui_tab_configuracion_grid_layout_1.addWidget(self._input_freq_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.gui_tab_configuracion_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.gui_tab_configuracion_grid_layout_1.setColumnStretch(c, 1)
        self._fs_range = Range(2000, 130000, 100, fs0, 200)
        self._fs_win = RangeWidget(self._fs_range, self.set_fs, 'Frecuencia de muestreo ', "counter_slider", float)
        self.gui_tab_configuracion_grid_layout_1.addWidget(self._fs_win, 1, 2, 1, 1)
        for r in range(1, 2):
            self.gui_tab_configuracion_grid_layout_1.setRowStretch(r, 1)
        for c in range(2, 3):
            self.gui_tab_configuracion_grid_layout_1.setColumnStretch(c, 1)
        _filtro_antialiasing_on_check_box = Qt.QCheckBox("Filtro antialiasing on")
        self._filtro_antialiasing_on_choices = {True: 1, False: 0}
        self._filtro_antialiasing_on_choices_inv = dict((v,k) for k,v in self._filtro_antialiasing_on_choices.iteritems())
        self._filtro_antialiasing_on_callback = lambda i: Qt.QMetaObject.invokeMethod(_filtro_antialiasing_on_check_box, "setChecked", Qt.Q_ARG("bool", self._filtro_antialiasing_on_choices_inv[i]))
        self._filtro_antialiasing_on_callback(self.filtro_antialiasing_on)
        _filtro_antialiasing_on_check_box.stateChanged.connect(lambda i: self.set_filtro_antialiasing_on(self._filtro_antialiasing_on_choices[bool(i)]))
        self.gui_tab_configuracion_grid_layout_0.addWidget(_filtro_antialiasing_on_check_box, 0, 3, 1, 1)
        for r in range(0, 1):
            self.gui_tab_configuracion_grid_layout_0.setRowStretch(r, 1)
        for c in range(3, 4):
            self.gui_tab_configuracion_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Output", #name
        	5 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.1, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['Salida filtro antialias', 'Salida sample and hold', 'Salida llave analogica', 'Salida filtro recuperador', 'Entrada',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "magenta", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(5):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	5 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(True)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not False)

        labels = ['Salida filtro antialias', 'Salida sample and hold', 'Salida llave analogica', 'Salida filtro recuperador', 'Entrada',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "magenta", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(5):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        _filtro_recuperador_on_check_box = Qt.QCheckBox("Filtro recuperador on")
        self._filtro_recuperador_on_choices = {True: 1, False: 0}
        self._filtro_recuperador_on_choices_inv = dict((v,k) for k,v in self._filtro_recuperador_on_choices.iteritems())
        self._filtro_recuperador_on_callback = lambda i: Qt.QMetaObject.invokeMethod(_filtro_recuperador_on_check_box, "setChecked", Qt.Q_ARG("bool", self._filtro_recuperador_on_choices_inv[i]))
        self._filtro_recuperador_on_callback(self.filtro_recuperador_on)
        _filtro_recuperador_on_check_box.stateChanged.connect(lambda i: self.set_filtro_recuperador_on(self._filtro_recuperador_on_choices[bool(i)]))
        self.gui_tab_configuracion_grid_layout_0.addWidget(_filtro_recuperador_on_check_box, 0, 2, 1, 1)
        for r in range(0, 1):
            self.gui_tab_configuracion_grid_layout_0.setRowStretch(r, 1)
        for c in range(2, 3):
            self.gui_tab_configuracion_grid_layout_0.setColumnStretch(c, 1)
        self.filtro_recuperador = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, freq0*18, freq0*18*0.5, firdes.WIN_HAMMING, 6.76))
        self.filtro_antialiasing = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, freq0*18, freq0*18*0.5, firdes.WIN_HAMMING, 6.76))
        self._dutycycle_range = Range(0.05, 0.95, 0.05, dutycycle0, 200)
        self._dutycycle_win = RangeWidget(self._dutycycle_range, self.set_dutycycle, 'Duty cycle', "counter_slider", float)
        self.gui_tab_configuracion_grid_layout_1.addWidget(self._dutycycle_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.gui_tab_configuracion_grid_layout_1.setRowStretch(r, 1)
        for c in range(1, 2):
            self.gui_tab_configuracion_grid_layout_1.setColumnStretch(c, 1)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('sen32.wav', True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_sample_and_hold_xx_0 = blocks.sample_and_hold_ff()
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((seniales_control_iguales, ))
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((-1, ))
        self.blks2_selector_1 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=seniales_control_iguales,
        	output_index=0,
        )
        self.blks2_selector_0_1 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=3,
        	num_outputs=1,
        	input_index=input_signal,
        	output_index=0,
        )
        self.blks2_selector_0_0_0_0 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=filtro_antialiasing_on,
        	output_index=0,
        )
        self.blks2_selector_0_0 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=switch_on,
        	output_index=0,
        )
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=syh_on,
        	output_index=0,
        )
        self.analog_sig_source_x_0_1_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, input_freq, 1, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, input_freq, 1, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_SQR_WAVE, fs, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blks2_selector_1, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blks2_selector_0_1, 1))
        self.connect((self.analog_sig_source_x_0_1_0, 0), (self.blks2_selector_0_1, 0))
        self.connect((self.blks2_selector_0, 0), (self.blks2_selector_0_0, 0))
        self.connect((self.blks2_selector_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blks2_selector_0_0, 0), (self.filtro_recuperador, 0))
        self.connect((self.blks2_selector_0_0_0_0, 0), (self.blks2_selector_0, 0))
        self.connect((self.blks2_selector_0_0_0_0, 0), (self.blocks_sample_and_hold_xx_0, 0))
        self.connect((self.blks2_selector_0_1, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blks2_selector_1, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_sample_and_hold_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blks2_selector_1, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blks2_selector_0_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_freq_sink_x_0, 2))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_sample_and_hold_xx_0, 0), (self.blks2_selector_0, 1))
        self.connect((self.blocks_sample_and_hold_xx_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.blocks_sample_and_hold_xx_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.blks2_selector_0_0_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.filtro_antialiasing, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 4))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_time_sink_x_0, 4))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blks2_selector_0_1, 2))
        self.connect((self.filtro_antialiasing, 0), (self.blks2_selector_0_0_0_0, 1))
        self.connect((self.filtro_antialiasing, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.filtro_antialiasing, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.filtro_recuperador, 0), (self.qtgui_freq_sink_x_0, 3))
        self.connect((self.filtro_recuperador, 0), (self.qtgui_time_sink_x_0, 3))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_fs0(self):
        return self.fs0

    def set_fs0(self, fs0):
        self.fs0 = fs0
        self.set_fs(self.fs0)

    def get_freq0(self):
        return self.freq0

    def set_freq0(self, freq0):
        self.freq0 = freq0
        self.set_input_freq(self.freq0)
        self.filtro_recuperador.set_taps(firdes.low_pass(1, self.samp_rate, self.freq0*18, self.freq0*18*0.5, firdes.WIN_HAMMING, 6.76))
        self.filtro_antialiasing.set_taps(firdes.low_pass(1, self.samp_rate, self.freq0*18, self.freq0*18*0.5, firdes.WIN_HAMMING, 6.76))

    def get_dutycycle0(self):
        return self.dutycycle0

    def set_dutycycle0(self, dutycycle0):
        self.dutycycle0 = dutycycle0
        self.set_dutycycle(self.dutycycle0)

    def get_syh_on(self):
        return self.syh_on

    def set_syh_on(self, syh_on):
        self.syh_on = syh_on
        self._syh_on_callback(self.syh_on)
        self.blks2_selector_0.set_input_index(int(self.syh_on))

    def get_switch_on(self):
        return self.switch_on

    def set_switch_on(self, switch_on):
        self.switch_on = switch_on
        self._switch_on_callback(self.switch_on)
        self.blks2_selector_0_0.set_input_index(int(self.switch_on))

    def get_seniales_control_iguales(self):
        return self.seniales_control_iguales

    def set_seniales_control_iguales(self, seniales_control_iguales):
        self.seniales_control_iguales = seniales_control_iguales
        self._seniales_control_iguales_callback(self.seniales_control_iguales)
        self.blocks_multiply_const_vxx_0.set_k((self.seniales_control_iguales, ))
        self.blks2_selector_1.set_input_index(int(self.seniales_control_iguales))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.filtro_recuperador.set_taps(firdes.low_pass(1, self.samp_rate, self.freq0*18, self.freq0*18*0.5, firdes.WIN_HAMMING, 6.76))
        self.filtro_antialiasing.set_taps(firdes.low_pass(1, self.samp_rate, self.freq0*18, self.freq0*18*0.5, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)

    def get_input_signal(self):
        return self.input_signal

    def set_input_signal(self, input_signal):
        self.input_signal = input_signal
        self._input_signal_callback(self.input_signal)
        self.blks2_selector_0_1.set_input_index(int(self.input_signal))

    def get_input_freq(self):
        return self.input_freq

    def set_input_freq(self, input_freq):
        self.input_freq = input_freq
        self.analog_sig_source_x_0_1_0.set_frequency(self.input_freq)
        self.analog_sig_source_x_0_1.set_frequency(self.input_freq)

    def get_fs(self):
        return self.fs

    def set_fs(self, fs):
        self.fs = fs
        self.analog_sig_source_x_0_0.set_frequency(self.fs)

    def get_filtro_recuperador_on(self):
        return self.filtro_recuperador_on

    def set_filtro_recuperador_on(self, filtro_recuperador_on):
        self.filtro_recuperador_on = filtro_recuperador_on
        self._filtro_recuperador_on_callback(self.filtro_recuperador_on)

    def get_filtro_antialiasing_on(self):
        return self.filtro_antialiasing_on

    def set_filtro_antialiasing_on(self, filtro_antialiasing_on):
        self.filtro_antialiasing_on = filtro_antialiasing_on
        self._filtro_antialiasing_on_callback(self.filtro_antialiasing_on)
        self.blks2_selector_0_0_0_0.set_input_index(int(self.filtro_antialiasing_on))

    def get_dutycycle(self):
        return self.dutycycle

    def set_dutycycle(self, dutycycle):
        self.dutycycle = dutycycle


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Mar 29 17:27:08 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print ("Warning: failed to XInitThreads()")

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
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
        self.freq0 = freq0 = 2500
        self.dutycycle0 = dutycycle0 = 0.5
        self.syh_on = syh_on = True
        self.switch_on = switch_on = True
        self.samp_rate = samp_rate = 120000
        self.input_freq = input_freq = freq0
        self.dutycycle = dutycycle = dutycycle0
        self.chooser = chooser = 0

        ##################################################
        # Blocks
        ##################################################
        _syh_on_check_box = Qt.QCheckBox("Sample and hold on")
        self._syh_on_choices = {True: 1, False: 0}
        self._syh_on_choices_inv = dict((v,k) for k,v in self._syh_on_choices.iteritems())
        self._syh_on_callback = lambda i: Qt.QMetaObject.invokeMethod(_syh_on_check_box, "setChecked", Qt.Q_ARG("bool", self._syh_on_choices_inv[i]))
        self._syh_on_callback(self.syh_on)
        _syh_on_check_box.stateChanged.connect(lambda i: self.set_syh_on(self._syh_on_choices[bool(i)]))
        self.top_grid_layout.addWidget(_syh_on_check_box)
        _switch_on_check_box = Qt.QCheckBox("Llave analogica on")
        self._switch_on_choices = {True: 1, False: 0}
        self._switch_on_choices_inv = dict((v,k) for k,v in self._switch_on_choices.iteritems())
        self._switch_on_callback = lambda i: Qt.QMetaObject.invokeMethod(_switch_on_check_box, "setChecked", Qt.Q_ARG("bool", self._switch_on_choices_inv[i]))
        self._switch_on_callback(self.switch_on)
        _switch_on_check_box.stateChanged.connect(lambda i: self.set_switch_on(self._switch_on_choices[bool(i)]))
        self.top_grid_layout.addWidget(_switch_on_check_box)
        self._input_freq_range = Range(freq0/10, freq0*10, freq0/100, freq0, 200)
        self._input_freq_win = RangeWidget(self._input_freq_range, self.set_input_freq, 'Frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._input_freq_win)
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Input", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_1.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_1_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Output", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self._dutycycle_range = Range(0.05, 0.95, 0.05, dutycycle0, 200)
        self._dutycycle_win = RangeWidget(self._dutycycle_range, self.set_dutycycle, 'Duty cycle', "counter_slider", float)
        self.top_grid_layout.addWidget(self._dutycycle_win)
        self._chooser_options = (0, 1, 2, )
        self._chooser_labels = (str(self._chooser_options[0]), str(self._chooser_options[1]), str(self._chooser_options[2]), )
        self._chooser_tool_bar = Qt.QToolBar(self)
        self._chooser_tool_bar.addWidget(Qt.QLabel("chooser"+": "))
        self._chooser_combo_box = Qt.QComboBox()
        self._chooser_tool_bar.addWidget(self._chooser_combo_box)
        for label in self._chooser_labels: self._chooser_combo_box.addItem(label)
        self._chooser_callback = lambda i: Qt.QMetaObject.invokeMethod(self._chooser_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._chooser_options.index(i)))
        self._chooser_callback(self.chooser)
        self._chooser_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_chooser(self._chooser_options[i]))
        self.top_grid_layout.addWidget(self._chooser_tool_bar)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_sample_and_hold_xx_0 = blocks.sample_and_hold_ff()
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
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
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_SQR_WAVE, 100000, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, input_freq, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blks2_selector_0, 0), (self.blks2_selector_0_0, 0))
        self.connect((self.blks2_selector_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blks2_selector_0_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_sample_and_hold_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blks2_selector_0_0, 1))
        self.connect((self.blocks_sample_and_hold_xx_0, 0), (self.blks2_selector_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.blks2_selector_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_sample_and_hold_xx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_freq0(self):
        return self.freq0

    def set_freq0(self, freq0):
        self.freq0 = freq0
        self.set_input_freq(self.freq0)

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

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_input_freq(self):
        return self.input_freq

    def set_input_freq(self, input_freq):
        self.input_freq = input_freq
        self.analog_sig_source_x_0.set_frequency(self.input_freq)

    def get_dutycycle(self):
        return self.dutycycle

    def set_dutycycle(self, dutycycle):
        self.dutycycle = dutycycle

    def get_chooser(self):
        return self.chooser

    def set_chooser(self, chooser):
        self.chooser = chooser
        self._chooser_callback(self.chooser)


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

import unittest
from unittest.mock import patch, MagicMock
import src.main as main

class TestMain(unittest.TestCase):
    @patch('src.main.read_speeds_from_file')
    @patch('src.main.populate_table')
    def test_update_data_1(self, mock_populate_table, mock_read_speeds_from_file):
        # Configura i mock
        mock_read_speeds_from_file.return_value = [10.0, 20.0, 30.0]
        
        # Chiama la funzione
        main.update_data_1('fake_path.txt')
        
        # Verifica che le funzioni siano state chiamate con i parametri corretti
        mock_read_speeds_from_file.assert_called_once_with('fake_path.txt')
        mock_populate_table.assert_called_once_with(main.table_1, [10.0, 20.0, 30.0], main.giroRuota)
        
    '''@patch('src.main.read_speeds_from_file')
    @patch('src.main.populate_table')
    def test_update_data_2(self, mock_populate_table, mock_read_speeds_from_file):
        # Configura i mock
        mock_read_speeds_from_file.return_value = [15.0, 25.0, 35.0]
        
        # Mock Tkinter components
        main.table_2 = None
        main.root = MagicMock()
        
        # Chiama la funzione
        main.update_data_2('fake_path.txt')
        
        # Verifica che le funzioni siano state chiamate con i parametri corretti
        mock_read_speeds_from_file.assert_called_once_with('fake_path.txt')
        self.assertTrue(mock_populate_table.called)
        
    @patch('src.main.FigureCanvasTkAgg')
    @patch('src.main.create_plot')
    def test_update_plot(self, mock_create_plot, mock_FigureCanvasTkAgg):
        # Configura i mock
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_create_plot.return_value = (mock_fig, mock_ax)
        mock_canvas = MagicMock()
        mock_FigureCanvasTkAgg.return_value = mock_canvas
        
        # Chiama la funzione
        main.update_plot()
        
        # Verifica che le funzioni siano state chiamate con i parametri corretti
        mock_create_plot.assert_called_once_with(main.speeds_1, main.giroRuota, main.speeds_2)
        self.assertTrue(mock_canvas.draw.called)
        self.assertTrue(mock_canvas.get_tk_widget().pack.called)
        
    @patch('src.main.update_table')
    @patch('src.main.highlight_point')
    def test_on_table1_click(self, mock_highlight_point, mock_update_table):
        # Configura i mock
        main.table_1 = MagicMock()
        main.table_2 = MagicMock()
        main.table_1.focus.return_value = 'focus_item_1'
        main.table_2.focus.return_value = 'focus_item_2'
        main.table_1.item.return_value = {'values': [100.0, 10.0]}
        
        # Chiama la funzione
        event = MagicMock()
        main.on_table1_click(event)
        
        # Verifica che le funzioni siano state chiamate con i parametri corretti
        self.assertTrue(mock_update_table.called)
        self.assertTrue(mock_highlight_point.called)
        
    @patch('src.main.update_table')
    @patch('src.main.highlight_point')
    def test_on_table2_click(self, mock_highlight_point, mock_update_table):
        # Configura i mock
        main.table_1 = MagicMock()
        main.table_2 = MagicMock()
        main.table_2.focus.return_value = 'focus_item_2'
        main.table_2.item.return_value = {'values': [200.0, 20.0]}
        
        # Chiama la funzione
        event = MagicMock()
        main.on_table2_click(event)
        
        # Verifica che le funzioni siano state chiamate con i parametri corretti
        self.assertTrue(mock_update_table.called)
        self.assertTrue(mock_highlight_point.called)
        
    @patch('src.main.highlight_point_from_plot_click')
    @patch('src.main.update_table')
    @patch('src.main.find_nearest_index')
    def test_on_plot_click(self, mock_find_nearest_index, mock_update_table, mock_highlight_point_from_plot_click):
        # Configura i mock
        mock_find_nearest_index.side_effect = [0, 1]
        main.speeds_1 = [10.0, 20.0, 30.0]
        main.speeds_2 = [15.0, 25.0, 35.0]
        
        # Chiama la funzione
        event = MagicMock()
        event.xdata = 3.0
        main.on_plot_click(event)
        
        # Verifica che le funzioni siano state chiamate con i parametri corretti
        self.assertTrue(mock_update_table.called)
        self.assertTrue(mock_highlight_point_from_plot_click.called)'''
        
        
if __name__ == '__main__':
    unittest.main()

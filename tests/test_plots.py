from src.medical_data_analysis import draw_cat_plot, draw_heat_map

def test_cat_plot():
    fig = draw_cat_plot()
    assert fig is not None

def test_heat_map():
    fig = draw_heat_map()
    assert fig is not None

import main



def test_smh():
    assert main.who_wins('s', 's') == 0
    assert main.who_wins('s', 'p') == 1
    assert main.who_wins('p','s') == 2



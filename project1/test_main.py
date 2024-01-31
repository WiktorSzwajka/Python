import main



def test_smh():
    assert main.who_wins('s', 's') == 0
    assert main.who_wins('s', 'r') == 2
    assert main.who_wins('s', 'p') == 1

    assert main.who_wins('p','s') == 2
    assert main.who_wins('p', 'r') == 1
    assert main.who_wins('p', 'p') == 0

    assert main.who_wins('r', 's') == 1
    assert main.who_wins('r', 'p') == 2
    assert main.who_wins('r', 'r') == 0
    
    assert main.who_wins('w', 'd') == -1



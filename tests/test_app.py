from .context import application_gateway


def test_app(capsys, example_fixture):
    # pylint: disable=W0612,W0613
    application_gateway.Blueprint.run()
    captured = capsys.readouterr()

    assert "Hello World..." in captured.out

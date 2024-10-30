
test = {
  'name': 'Question 1_p',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # pou need to set the value for 'p'
          >>> assert 'p' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert p == -8
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}


test = {
  'name': 'Question 1_y',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'y'
          >>> assert 'y' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert y == "That's right"
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

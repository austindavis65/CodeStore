MAX_LEAD_LENGTH = 10
MAX_NUM_LEADS = 5

class Pencil:
    """Represent a mechanical pencil with leads in its barrel."""

    def __init__(self, num_leads):
        """Initialize a pencil.

        Data members:
        _num_leads -- the number of lead sticks in the barrel of the
            pencil.
        _current_lead_length -- the length of the lead stick extending
            from the pencil.
        """
        self._num_leads = 0
        self._current_lead_length = MAX_LEAD_LENGTH
        self.add_leads(num_leads)

    def get_num_leads(self):
        """Return the number of leads in the pencil.

        This does not count the lead that is extending from the pencil.
        """
        return self._num_leads

    def get_current_lead_length(self):
        """Return the length of the lead extending from the pencil."""
        return self._current_lead_length

    def click(self):
        """Click the pencil, reducing the current lead length by one.

        If the current lead is used up, reduce the number of leads in
        the pencil by one and set the current lead length to the max
        lead length.
        """
        if self._current_lead_length > 0:
            self._current_lead_length -= 1
        if self._current_lead_length == 0 and self._num_leads > 0:
            self._current_lead_length = MAX_LEAD_LENGTH
            self._num_leads -= 1
        return self._current_lead_length > 0

    def add_leads(self, num_additional_leads):
        """Add leads to the pencil.

        Only add a positive number of leads, up to the maximum number
        of leads.
        """
        if num_additional_leads > 0:
            self._num_leads += num_additional_leads
            if self._num_leads > MAX_NUM_LEADS:
                self._num_leads = MAX_NUM_LEADS
        return self._num_leads

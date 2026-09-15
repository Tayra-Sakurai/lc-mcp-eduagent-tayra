# SPDX-FileCopyrightText: 2026 Tayra Sakurai
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Solution analysis module."""


def convert_to_volume_molar(
    weight_percentage: float,
    density: float,
    mw: float
) -> float:
    """Converts the weight percentage to molarity.

    Parameters
    ----------
    weight_percentage : float
        The weight percentage of the solution.
    density : float
        The density of the solution.
    mw : float
        The molecular weight of the solute.

    Returns
    -------
    molarity : float
        The molarity.
    """
    return (10 * density * weight_percentage) / mw


def pixel_to_ratio(
    x,
    y,
    reference_rect=None,
    img_width=160,
    img_height=120,
    target_width=320,
    target_height=240,
):
    """
    Map pixel coordinates (x, y) from a source image or ROI to a target resolution.

    Args:
        x: Source x coordinate.
        y: Source y coordinate.
        reference_rect: Optional (x, y, w, h) tuple defining a region of interest in the source.
                        If provided, coordinates are normalized relative to this rect.
        img_width: Source image width (used if reference_rect is None).
        img_height: Source image height (used if reference_rect is None).
        target_width: Width of the target coordinate space.
        target_height: Height of the target coordinate space.

    Returns:
        Tuple (target_x, target_y) mapped to the target resolution.
    """
    if reference_rect:
        rx, ry, rw, rh = reference_rect
        # Avoid division by zero
        x_norm = (x - rx) / rw if rw > 0 else 0
        y_norm = (y - ry) / rh if rh > 0 else 0
    else:
        # Avoid division by zero
        x_norm = x / img_width if img_width > 0 else 0
        y_norm = y / img_height if img_height > 0 else 0

    # Clamp values between 0 and 1
    x_norm = max(0.0, min(1.0, x_norm))
    y_norm = max(0.0, min(1.0, y_norm))

    return (x_norm * target_width, y_norm * target_height)

def run_tests():
    # Test 1: Normal full image
    res = pixel_to_ratio(80, 60, img_width=160, img_height=120, target_width=320, target_height=240)
    assert res == (160.0, 120.0), f"Test 1 failed: {res}"
    print("Test 1 passed")

    # Test 2: ROI
    res = pixel_to_ratio(60, 60, reference_rect=(10, 10, 100, 100), target_width=100, target_height=100)
    # (60-10)/100 = 0.5. Target 100 -> 50.
    assert res == (50.0, 50.0), f"Test 2 failed: {res}"
    print("Test 2 passed")

    # Test 3: Clamping
    res = pixel_to_ratio(200, 200, img_width=100, img_height=100, target_width=100, target_height=100)
    assert res == (100.0, 100.0), f"Test 3 failed: {res}"
    
    res = pixel_to_ratio(-10, -10, img_width=100, img_height=100, target_width=100, target_height=100)
    assert res == (0.0, 0.0), f"Test 3b failed: {res}"
    print("Test 3 passed")

    # Test 4: Zero division
    res = pixel_to_ratio(10, 10, img_width=0, img_height=0)
    assert res == (0.0, 0.0), f"Test 4 failed: {res}"
    print("Test 4 passed")

if __name__ == "__main__":
    run_tests()

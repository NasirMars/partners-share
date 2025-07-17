# Python code to calculate monthly investment distribution
# Run this in Google Colab or any Python environment

# Define the variables here. Replace with your actual values.
F_start = 10000.0  # Beginning capital for F
L_start = 1000.0  # Beginning capital for L
Z_start = 1000.0  # Beginning capital for Z
total_end = 19000.0  # Total capital at the end of the month

# Calculate total starting capital
total_start = F_start + L_start + Z_start
print(f"Total starting capital: {total_start:.2f}")

if total_start <= 0:
    print("Total beginning capital must be positive.")
else:
    # Calculate gain percentage
    gain_pct = ((total_end - total_start) / total_start) * 100 if total_start > 0 else 0.0
    print(f"Monthly gain: {gain_pct:.2f}%")

    # Proportions
    proportions = {
        'F': F_start / total_start,
        'L': L_start / total_start,
        'Z': Z_start / total_start
    }
    print("\nProportions:")
    for person, prop in proportions.items():
        print(f"{person}: {prop:.4f} ({F_start:.2f}/{total_start:.2f} for F, etc.)")

    # Total profit or loss
    profit = total_end - total_start
    print(f"\nTotal profit/loss: {profit:.2f}")

    finals = {}
    if profit <= 0:
        print("Loss or no gain. Distributing by proportion.")
        finals['F'] = proportions['F'] * total_end
        finals['L'] = proportions['L'] * total_end
        finals['Z'] = proportions['Z'] * total_end
        print("\nDetails:")
        print(f"F: proportion {proportions['F']:.4f} * total_end {total_end:.2f} = {finals['F']:.2f}")
        print(f"L: proportion {proportions['L']:.4f} * total_end {total_end:.2f} = {finals['L']:.2f}")
        print(f"Z: proportion {proportions['Z']:.4f} * total_end {total_end:.2f} = {finals['Z']:.2f}")
    else:
        # Determine fee rate
        if 0 < gain_pct < 40:
            fee_rate = 0.2
        elif gain_pct >= 40:
            fee_rate = 0.3
        else:
            fee_rate = 0  # Should not happen if profit > 0

        print(f"Gain positive. Applying performance fee to F at rate: {fee_rate * 100:.0f}%")

        # Individual profits
        profits = {
            'F': proportions['F'] * profit,
            'L': proportions['L'] * profit,
            'Z': proportions['Z'] * profit
        }
        print("\nIndividual profits before fees:")
        for person, prof in profits.items():
            print(f"{person}: proportion {proportions[person]:.4f} * total profit {profit:.2f} = {prof:.2f}")

        # Fees
        fee_from_L = fee_rate * profits['L']
        fee_from_Z = fee_rate * profits['Z']
        print("\nFees paid to F:")
        print(f"From L: {fee_rate * 100:.0f}% of L's profit {profits['L']:.2f} = {fee_from_L:.2f}")
        print(f"From Z: {fee_rate * 100:.0f}% of Z's profit {profits['Z']:.2f} = {fee_from_Z:.2f}")

        # Final amounts
        finals['F'] = F_start + profits['F'] + fee_from_L + fee_from_Z
        finals['L'] = L_start + profits['L'] - fee_from_L
        finals['Z'] = Z_start + profits['Z'] - fee_from_Z

        print("\nFinal calculations:")
        print(f"F: start {F_start:.2f} + profit {profits['F']:.2f} + fee from L {fee_from_L:.2f} + fee from Z {fee_from_Z:.2f} = {finals['F']:.2f}")
        print(f"L: start {L_start:.2f} + profit {profits['L']:.2f} - fee {fee_from_L:.2f} = {finals['L']:.2f}")
        print(f"Z: start {Z_start:.2f} + profit {profits['Z']:.2f} - fee {fee_from_Z:.2f} = {finals['Z']:.2f}")

    # Print the results
    print("\nFinal amounts:")
    for person, amount in finals.items():
        print(f"{person} should get: {amount:.2f}")

    # Check if the sum matches total_end
    total_final = sum(finals.values())
    print(f"Total distributed: {total_final:.2f} (should match end capital {total_end:.2f})")

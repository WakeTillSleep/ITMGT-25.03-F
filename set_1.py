def savings(gross_pay, tax_rate, expenses):
    after_tax = int(gross_pay * (1 - tax_rate))
    return after_tax - expenses

def material_waste(total_material, material_units, num_jobs, job_consumption):
    used = num_jobs * job_consumption
    waste = total_material - used
    return f"{waste}{material_units}"

def interest(principal, rate, periods):
    final_amount = principal + (principal * rate * periods)
    return int(final_amount)
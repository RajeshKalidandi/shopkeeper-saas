'use client'

import { DashboardShell } from '@/components/layout/dashboard-shell'
import { useAuth } from '@/hooks/useAuth'
import {
  ArrowTrendingUpIcon,
  CurrencyRupeeIcon,
  ShoppingBagIcon,
  UserGroupIcon,
} from '@heroicons/react/24/outline'
import { useEffect } from 'react'

const stats = [
  {
    id: 1,
    name: 'Total Revenue',
    stat: '₹72,000',
    icon: CurrencyRupeeIcon,
    change: '12%',
    changeType: 'increase',
  },
  {
    id: 2,
    name: 'Total Products',
    stat: '256',
    icon: ShoppingBagIcon,
    change: '2.3%',
    changeType: 'increase',
  },
  {
    id: 3,
    name: 'Active Customers',
    stat: '98',
    icon: UserGroupIcon,
    change: '4.5%',
    changeType: 'increase',
  },
  {
    id: 4,
    name: 'Growth Rate',
    stat: '24.5%',
    icon: ArrowTrendingUpIcon,
    change: '3.2%',
    changeType: 'increase',
  },
]

export default function DashboardPage() {
  const { user, getUser } = useAuth()

  useEffect(() => {
    getUser()
  }, [getUser])

  return (
    <DashboardShell>
      <div className="space-y-8">
        <div>
          <h2 className="text-2xl font-bold leading-tight tracking-tight text-gray-900">
            Welcome back, {user?.first_name}!
          </h2>
          <p className="mt-2 text-sm text-gray-600">
            Here&apos;s what&apos;s happening with your shop today.
          </p>
        </div>

        <div>
          <dl className="mt-5 grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
            {stats.map((item) => (
              <div
                key={item.id}
                className="relative overflow-hidden rounded-lg bg-white px-4 pb-12 pt-5 shadow sm:px-6 sm:pt-6"
              >
                <dt>
                  <div className="absolute rounded-md bg-primary-500 p-3">
                    <item.icon
                      className="h-6 w-6 text-white"
                      aria-hidden="true"
                    />
                  </div>
                  <p className="ml-16 truncate text-sm font-medium text-gray-500">
                    {item.name}
                  </p>
                </dt>
                <dd className="ml-16 flex items-baseline pb-6 sm:pb-7">
                  <p className="text-2xl font-semibold text-gray-900">
                    {item.stat}
                  </p>
                  <p
                    className={`ml-2 flex items-baseline text-sm font-semibold text-green-600`}
                  >
                    <span className="sr-only">
                      {item.changeType === 'increase'
                        ? 'Increased by'
                        : 'Decreased by'}
                    </span>
                    {item.change}
                  </p>
                  <div className="absolute inset-x-0 bottom-0 bg-gray-50 px-4 py-4 sm:px-6">
                    <div className="text-sm">
                      <a
                        href="#"
                        className="font-medium text-primary-600 hover:text-primary-500"
                      >
                        View details
                        <span className="sr-only"> {item.name} stats</span>
                      </a>
                    </div>
                  </div>
                </dd>
              </div>
            ))}
          </dl>
        </div>
      </div>
    </DashboardShell>
  )
}
